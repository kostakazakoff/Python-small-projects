from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import requests
from decimal import Decimal
from forex_python.converter import CurrencyRates


def exchange(source_currency: str, destination_currency: str, amount: Decimal):
    currencies = CurrencyRates()
    rate = Decimal(currencies.get_rate(source_currency, destination_currency))
    return f'{amount * rate:.2f}'


def country_prices(country: str, item: str, currency: str):
    prices_url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"
    querystring = {"country_name": country}
    headers = {
        "X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
        "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
    }
    response = requests.request("GET", prices_url, headers=headers, params=querystring)
    data = response.json()
    prices = data['prices']

    item_name, item_min_price, item_max_price, \
    item_average_price = 'Not defined', 'Not defined', 'Not defined', 'Not defined'
    output = [f'Prices in {country}:']

    for i in range(len(prices)):
        if prices[i]['item_name'] == item:
            item_name = item
            item_min_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['min']))
            item_max_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['max']))
            item_average_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['avg']))
            break

    output.append(f'\n{item_name}:\nmin price: {item_min_price} {currency}, max price: {item_max_price} {currency}, '
                  f'average price: {item_average_price} {currency}')
    return ''.join(output)


class MainWidget(Widget):
    input_country = ObjectProperty(None)
    input_item = ObjectProperty(None)
    currency_input = ObjectProperty(None)

    def submit_press(self):
        input_country = self.ids.input_country.text
        input_item = self.ids.input_item.text
        currency_input = self.ids.input_currency.text
        self.ids.output_box.text = country_prices(input_country, input_item, currency_input)


class WorldPricesExplore(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    WorldPricesExplore().run()
