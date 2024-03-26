# File where the APi's models will be store 
from pydantic import BaseModel, Field

class Product(BaseModel):
  id: int = Field(..., gt=0, description="The unique identifier for the product")
  name: str = Field(..., min_length=1, max_length=50, description="The name of the product")
  description: str = Field(..., min_length=1, max_length=150, description="The description of the product")
  price: float = Field(..., gt=0, description="The price of the product must be greater than 0")
  
