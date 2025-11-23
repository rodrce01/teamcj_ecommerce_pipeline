#asychronously fetch/scrape product data
#uses aiohttp/asyncio for concurrent requests
#using real-time-amazon-data API from OpenWeb Ninja
import requests

url = "https://real-time-amazon-data.p.rapidapi.com/product-review-details"

querystring = {"review_id":"RYRK6K6MMXB9C","country":"US"}

headers = {
	"x-rapidapi-key": "953d586932msh91b3af1832b66a6p106484jsnb9956f4a03a1",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())