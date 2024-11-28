# create Catalog class
from typing import Optional
from pydantic import BaseModel


class CatalogItem(BaseModel):
    item_id: int
    item_name: str
    isbn_num: str
    author: str
    publisher: str
    release_date: str
    genre: str
    num_of_copies: int
    format: str
    num_of_pages: int
    description: Optional[str] = None
    item_availability: bool = None
