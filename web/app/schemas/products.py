import datetime

from pydantic.main import BaseModel


class ProductSchema(BaseModel):
    created_at: datetime.datetime
    name: str
    description: str
    sku: int
    price: int
