from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path

app = FastAPI()
BASE_DIR = Path(__file__).parent.parent

@app.get("/", response_class=HTMLResponse)
async def home():
    return (BASE_DIR / "static/index.html").read_text()
