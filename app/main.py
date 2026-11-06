from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.config import BASE_DIR
from app.api.upload import router as upload_router
from app.api.analytics import router as analytics_router
from app.api.chat import router as chat_router

app = FastAPI(title='AI Data Analyst Agent', version='0.1.0')
app.include_router(upload_router, prefix='/api')
app.include_router(analytics_router, prefix='/api')
app.include_router(chat_router, prefix='/api')
app.mount('/static', StaticFiles(directory=BASE_DIR / 'frontend'), name='static')

@app.get('/')
def home():
    return FileResponse(BASE_DIR / 'frontend' / 'index.html')

@app.get('/health')
def health():
    return {'status': 'ok'}
