from fastapi import APIRouter, HTTPException
from app.services.file_service import get_dataset
from app.services.data_service import summarize
from app.agents.visualization_agent import build_chart
router = APIRouter()

@router.get('/analytics/{dataset_id}')
def analytics(dataset_id: str):
    return summarize(get_dataset(dataset_id))

@router.get('/chart/{dataset_id}/{column}')
def chart(dataset_id: str, column: str):
    try:
        return {'chart_json': build_chart(get_dataset(dataset_id), column)}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
