from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_dataset
from app.services.data_service import profile
router = APIRouter()

@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    dataset_id, df = await save_dataset(file)
    return {'dataset_id': dataset_id, 'profile': profile(df)}
