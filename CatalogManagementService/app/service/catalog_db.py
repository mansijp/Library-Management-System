from model import catalog

# connect to database (using lists for now)
catalog_list = []


def add_item_db(item: catalog.CatalogItem):
    catalog_list.append(item.dict())
    print(catalog_list)
