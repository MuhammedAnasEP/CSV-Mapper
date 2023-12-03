from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates('templates')


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})