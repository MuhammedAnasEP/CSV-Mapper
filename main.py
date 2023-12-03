from fastapi import FastAPI, Request, File, UploadFile, Depends
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import csv
import codecs

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

@app.post('/upload')
async def upload(request: Request, file: UploadFile = File(...), db: Session = Depends(get_db)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    print(csvReader)

    datas = []

    for row in csvReader:
        dic = {}
        for key, value in row.items():
            new_key = key
            new_key = new_key.lower()
            new_key = new_key.replace(" ", "")
            dic[new_key] = value
        datas.append(dic)
        
    
    for rows in datas:
        name = rows["name"]
        age = rows["age"]
        new_user = models.User(name=name, age=int(age))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    
    file.file.close()
    return templates.TemplateResponse("home.html", {"request": request,"message":"The name and age in csv file uploaded succesfully."})