import requests

def lambda_handler():
    simple_grocery_url = "https://simple-grocery-store-api.glitch.me/products?results=20&available=true"
    response = requests.get(url=simple_grocery_url)
    return response.json()