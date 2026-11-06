from pathlib import Path
from uuid import uuid4
import pandas as pd
from fastapi import UploadFile, HTTPException
from app.config import UPLOAD_DIR, MAX_FILE_SIZE

ALLOWED = {'.csv', '.xlsx'}

def load_dataframe(path: Path) -> pd.DataFrame:
    if path.suffix == '.csv':
        return pd.read_csv(path)
    return pd.read_excel(path, engine='openpyxl')

async def save_dataset(file: UploadFile):
    suffix = Path(file.filename or '').suffix.lower()
    if suffix not in ALLOWED:
        raise HTTPException(400, 'Only .csv and .xlsx files are supported')
    content = await file.read(MAX_FILE_SIZE + 1)
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(413, 'Maximum file size is 10 MB')
    dataset_id = uuid4().hex
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    path = UPLOAD_DIR / f'{dataset_id}{suffix}'
    path.write_bytes(content)
    try:
        df = load_dataframe(path)
        if df.empty or len(df.columns) == 0:
            raise ValueError('Dataset must contain data and columns')
    except Exception as exc:
        path.unlink(missing_ok=True)
        raise HTTPException(400, f'Unable to read dataset: {exc}') from exc
    return dataset_id, df

def get_dataset(dataset_id: str):
    if len(dataset_id) != 32 or not all(c in '0123456789abcdef' for c in dataset_id):
        raise HTTPException(400, 'Invalid dataset ID')
    matches = list(UPLOAD_DIR.glob(f'{dataset_id}.*'))
    if not matches:
        raise HTTPException(404, 'Dataset not found')
    return load_dataframe(matches[0])
