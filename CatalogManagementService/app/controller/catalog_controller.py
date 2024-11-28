# create item
# read item
# update item
# delete item
from fastapi import FastAPI, APIRouter
from typing import List
from model import catalog
from service import catalog_db

router = APIRouter()

# routes


# create an item
@router.post("/item", response_model=catalog.CatalogItem)
def add_item(item: catalog.CatalogItem):
    catalog_db.add_item_db(item)  # send to Service to add to database
    return item
