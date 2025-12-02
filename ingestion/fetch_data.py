#asychronously fetch/scrape product data
#uses aiohttp/asyncio for concurrent requests
#using real-time-amazon-data API from OpenWeb Ninja
#http status codes for success:
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
#list of best endpoints to use: 
import requests
import json

Searchurl = "https://real-time-amazon-data.p.rapidapi.com/search" #after / is endpoint listed in api
#other options: products-by-category, product-details, product-reviews, product-review-details, top-product-reviews, product-offers
#more: 
#Sellers: seller-profile, seller-reviews, seller-products
#deals and best sellers: best-sellers, deals-v2, deal-products, promo-code-details
#don't know if i need to use influencers: influencer-profile, influencer-posts, influencer-post-products
# or utility: asin-to-gtin, product-category-list

querystring = {"query":"Phone","page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}
#searching for phone, first page of results, in US only, not only prime, any condition, not only deals/discounts
headers = {
	"x-rapidapi-key": "953d586932msh91b3af1832b66a6p106484jsnb9956f4a03a1",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(Searchurl, headers=headers, params=querystring)

print(response.json()) 
#will have data scraping from individual stuff to plug in
