# File where the APi's models will be store 
from pydantic import BaseModel

class Product(BaseModel):
  id: int
  name: str
  description: str
  price: float
  
