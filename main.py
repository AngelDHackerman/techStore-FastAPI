from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models import Product

app = FastAPI()

@app.get('/')
def read_root():
  return {"Hello": "World"}