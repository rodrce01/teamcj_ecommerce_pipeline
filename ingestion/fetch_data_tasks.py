#asychronously fetch/scrape product data
#list of tasks as well
#uses aiohttp/asyncio for concurrent requests
#using real-time-amazon-data API from OpenWeb Ninja
#https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data
#https://www.openwebninja.com/api/real-time-amazon-data/docs
#http status codes for success:
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

#db_connection.py connects to MongoDB database
import requests
import json
import http.client
from celery_app.celery import celery_app
#class Fetch_data #I don't know if this is necessary
#url = the endpoint, headers = api key that remains the same, querystring = list of conditions. query is what the user types in.
#fetchdata using this

#specifically search task
@celery_app.task
def get_search_data(searchTerm, pagenum, nation, sort_by, department, departmentNum, minPrice, maxPrice, productCondition, primeYN, deals, fourOrMoreStars, language, more_filters, searchFields): #have terms in search conditions within the ()
    #get data f
    requests.get(
        "https://api.openwebninja.com/realtime-amazon-data/search",
        headers={
            "x-api-key": "953d586932msh91b3af1832b66a6p106484jsnb9956f4a03a1"
        },
        params={
            "query": "Phone",
            "page": "1",
            "country": "US",
            "sort_by": "NEWEST",
            "category_id": "aps (All Departments)",
            "category": "2858778013",
            "min_price": "105",
            "max_price": "110",
            "product_condition": "NEW",
            "is_prime": "FALSE",
            "deals_and_discounts": "NONE",
            "four_stars_and_up": "TRUE",
            "language": "en_US",
            "additional_filters": "p_n_feature_browse-bin%3A2656022011",
            "fields": "product_price,product_url,is_best_seller,sales_volume"
        }
    )
@celery_app.task
def get_product_category_list(country): #takes country to determine available products
    requests.get(
        "https://api.openwebninja.com/realtime-amazon-data/product-category-list",
        headers={
            "x-api-key": "953d586932msh91b3af1832b66a6p106484jsnb9956f4a03a1"
        },
        params={
            "country": country #US default, Sets the Amazon domain, marketplace country, language and currency.
        }
    )
@celery_app.task
def get_asinORgtin():
    #asin-to-gtin for the end of the link

#specifically task to get data for product category list
originalurl = "api.openwebninja.com/realtime-amazon-data/"
productArray = ["search", "products-by-category", "product-details", "product-reviews", "product-review-details", "top-product-reviews", "product-offers"]
sellerArray = ["seller-profile", "seller-reviews", "seller-products"] #possibly seller pages
dealBestSellerArray = ["best-sellers", "deals-v2", "deal-products", "promo-code-details"] #maybe another page
utilityArray = ["asin-to-gtin", "product-category-list"] #asin is the amazon id for products
#don't know if i need to use influencers: influencer-profile, influencer-posts, influencer-post-products. Do not use, this is what we want to avoid.
# or utility: asin-to-gtin, product-category-list. Also what to avoid.
        
#searching for phone, first page of results, in US only, not only prime, any condition, not only deals/discounts
#get categories first to see what is available. US default
#alternative response gotten from rapid api instead of original site

response = requests.get(searchurl, headers=headers, params=querystring)
categoryResponse = requests.get(categorylisturl, headers=headers, params=categoryquerystring)
#headers and response are standard.
jsonResult = response.json()  #not printing because it's too much
categoryJson = categoryResponse.json()
print(categoryJson)
print(jsonResult)
#will have data scraping from individual stuff to plug in
