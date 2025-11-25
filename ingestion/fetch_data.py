#asychronously fetch/scrape product data
#uses aiohttp/asyncio for concurrent requests
#using real-time-amazon-data API from OpenWeb Ninja
#http status codes for success:
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
#list of best endpoints to use: 
import requests

url = "https://real-time-amazon-data.p.rapidapi.com/search" #after / is endpoint listed in api

querystring = {"query":"Phone","page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}

headers = {
	"x-rapidapi-key": "953d586932msh91b3af1832b66a6p106484jsnb9956f4a03a1",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
base_url = "https://real-time-amazon-data.p.rapidapi.com/"
def get_amazon_info(variable): #haven't decided on variable yet
    url = f"{base_url}/search{variable}" #variations galore!!!
    response1 = requests.get(url)
    print(response1)

    if response1.status_code ==200: #200 is ok
        amazon_data = response1.json()
        return amazon_data
    else:
        print(f"failed to retrieve data: {response1.status_code}")

amazon_var = "phone" #example
amazon_info = get_amazon_info(amazon_var)
if amazon_info:
    print(f"Variable: {amazon_info["variable"]}") #variable is given variable. can return price, color, vendor, etc.
    #may need to be lowercase, uppercase, standardized
