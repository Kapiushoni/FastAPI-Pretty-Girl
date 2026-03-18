from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pretty Girl API")

# Указываем папку с HTML файлом
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Теперь при заходе на сайт сразу будет открываться твой красивый интерфейс
    return templates.TemplateResponse("index.html", {"request": request})