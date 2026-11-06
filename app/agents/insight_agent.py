from app.services.ai_service import explain

async def run(question, summary):
    return await explain(question, summary)
