from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Gắn folder static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Gắn folder templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route dự phòng tránh lỗi 404
@app.get("/{full_path:path}")
async def catch_all(request: Request, full_path: str):
    return templates.TemplateResponse("index.html", {"request": request})