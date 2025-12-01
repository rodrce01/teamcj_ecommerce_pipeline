#market basket analysis / trend detections
#we could use scikit-learn, pandas, etc.

from db_connection import db

def get_top_categories():
    #example funct to get top product categories
    collection = db['cleaned_products']
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    return list(collection.aggregate(pipeline))
