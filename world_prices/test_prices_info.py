import requests

url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"

querystring = {"city_name": "Bratislava", "country_name": "Slovakia"}

headers = {
    "X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
    "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
info = data['prices']

items = [info[i]['item_name'] for i in range(len(info))]
print(items)
