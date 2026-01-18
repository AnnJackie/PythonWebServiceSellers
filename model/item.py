from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int]
    seller_id: int
    item_name: str
    price: float