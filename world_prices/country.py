import requests


def country_prices():
    response = requests.request("GET", prices_url, headers=headers, params=querystring)
    data = response.json()
    prices = data['prices']
    currency = prices[-1]["currency_code"]
    print(f'Prices in {country} in {currency}:')
    print('----------------------------------------------------------------------------------')
    for i in range(len(prices)):
        item_name = prices[i]["item_name"]
        item_min_price = prices[i]['min']
        item_max_price = prices[i]['max']
        item_average_price = prices[i]['avg']
        print(f'{item_name}: min price: {item_min_price}, max price: {item_max_price}, '
              f'average price: {item_average_price}')


country = input('Country: ')

prices_url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"
querystring = {"country_name": country}
headers = {
    "X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
    "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
}

country_prices()