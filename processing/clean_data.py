#cleans product and sales data, ex: removing duplicates

from db_connection import db

def insert_cleaned_product(product):
    #insert a cleaned product into the 'cleaned_products' collection
    collection = db['cleaned_products']
    collection.insert_one(product)

def get_all_products():
    #fetch all products from the 'raw_products' collection
    collection = db['raw_products']
    return list(collection.find())
