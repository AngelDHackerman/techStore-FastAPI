from fastapi import FastAPI, HTTPException
from typing import List, Optional
import json
from pydantic import BaseModel
from models.models import Product

app = FastAPI()

# Read the JSON file
def load_users():
  with open('./utils/users.json', 'r') as file:  # todo: necesito que chat-gpt me explique este codigo
    return json.load(file)

# Create the endpoint GET 
@app.get("/api/users")
def get_users(page: int = 1, per_page: int = 6): # todo: necesito que chat-gpt me explique este codigo
  # paginate the results
  users = load_users()
  total_users = len(users)
  total_pages = (total_users - 1) // per_page + 1 # todo: necesito que chat-gpt me explique este codigo
  if page > total_pages or page < 1:
    raise HTTPException(status_code=404, detail='Page not found')
  
  start = (page - 1) * per_page
  end = start + per_page
  users_on_page = users[start:end] # todo: necesito que chat-gpt me explique este codigo

  # return with the paginated data
  return { 
    "page": page,
    "per_page": per_page,
    "total": total_users,
    "total_pages": total_pages,
    "data": users_on_page,
  }