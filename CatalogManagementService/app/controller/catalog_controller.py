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


# update number of copies
@router.put("/item/{num_of_copies}", response_model=catalog.CatalogItem)
def update_item():
    return {"message": "item updated", "number of copies": num_of_copies}


# check item availability by item_name
@router.get("/item/{item_name}", response_model=catalog.CatalogItem)
def check_availability():
    availability = True
    return availability


# search for item by item_id
@router.get("/item/{item_id}", response_model=catalog.CatalogItem)
def search_by_itemId():
    return "item info"


# search for item by item_name
@router.get("/item/{item_name}", response_model=catalog.CatalogItem)
def search_by_itemName():
    return "item info"


# search for item by author
@router.get("/item/{author}", response_model=catalog.CatalogItem)
def search_by_author():
    return "item info"


# search for item by isbn_num
@router.get("/item/{isbn_num}", response_model=catalog.CatalogItem)
def search_by_isbnNum():
    return "item info"


# remove item by item_id (only the manager can run this function)
@router.delete("/item/{item_id}", response_model=catalog.CatalogItem)
def delete_item():
    return {"message": "Item deleted successfully!"}


'''
- This should be done in manager management. Only the manager can access this service 
  so we don't need to allow access again.
  
# allow manager to access catalog
@router.get("/manager/{manager_id}", response_model=catalog.CatalogItem)
def allow_manager_access():
    return {"message": "Welcome back!"}'''
