from pydantic import BaseModel, Field
from typing import Optional

class Update_customer_request(BaseModel):
      name: str = Field(...,description="Customer name",min_length=3,max_length=50)
      phone: Optional[int] = Field(None ,description="Customer phone number")