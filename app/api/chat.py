from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.file_service import get_dataset
from app.workflows.analyst_workflow import run
from app.utils.validation import validate_question
router = APIRouter()

class ChatRequest(BaseModel):
    dataset_id: str
    question: str

@router.post('/chat')
async def chat(request: ChatRequest):
    try:
        question = validate_question(request.question)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return await run(get_dataset(request.dataset_id), question)
