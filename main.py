from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine

app = FastAPI()

templates = Jinja2Templates('templates')

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})