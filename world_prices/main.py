from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import requests
from decimal import Decimal
from forex_python.converter import CurrencyRates

Builder.load_file('ui.kv')


def exchange(source_currency: str, destination_currency: str, amount: Decimal):
    currencies = CurrencyRates()
    rate = Decimal(currencies.get_rate(source_currency, destination_currency))
    return f'{amount * rate:.2f}'


def request_prices(country):
    prices_url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"
    querystring = {"country_name": country}
    headers = {
        "X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
        "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
    }
    response = requests.request("GET", prices_url, headers=headers, params=querystring)
    data = response.json()
    return data['prices']


def request_cities():
    url = "https://cost-of-living-and-prices.p.rapidapi.com/cities"

    headers = {
        "X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
        "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()


def country_prices(country: str, item: str, currency: str):
    prices = request_prices(country)
    item_name, item_min_price, item_max_price, item_average_price, attention_message \
        = 'Not defined', 'Not defined', 'Not defined', 'Not defined', ''
    output = []

    for i in range(len(prices)):
        if prices[i]['item_name'] == item:
            try:
                item_min_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['min']))
                item_max_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['max']))
                item_average_price = exchange(prices[-1]["currency_code"], currency, Decimal(prices[i]['avg']))
            except:
                item_min_price = prices[i]['min']
                item_max_price = prices[i]['max']
                item_average_price = prices[i]['avg']
                currency = prices[-1]["currency_code"]
                attention_message = 'No currency exchange rate available'
            break

    output.append(f'\n{item}:\nmin: {item_min_price} {currency}, max: {item_max_price} {currency}, '
                  f'average: {item_average_price} {currency}\n{attention_message}')
    return ''.join(output)


cities = request_cities()
cities = cities['cities']


class MainWidget(Widget):
    input_country = ObjectProperty(None)
    input_item = ObjectProperty(None)
    currency_input = ObjectProperty(None)

    countries = sorted(set([cities[i]["country_name"] for i in range(len(cities))]))

    # items = [request_prices(input_country)[i]['item_name'] for i in range(len(request_prices(input_country)))]
    items = sorted(['Price per square meter to Buy Apartment Outside of City Center',
                    'Price per square meter to Buy Apartment in City Center',
                    'International Primary School, Yearly for 1 Child',
                    'Private Preschool or Kindergarten, Monthly for 1 Child',
                    'Pair of Jeans in a Chain Store Like George, H&M, Zara, etc.',
                    'Pair of Leather Business Shoes', 'Pair of Running Shoes, Mid-Range Price',
                    'Apples, 1 kg', 'Banana, 1 kg', 'Beef Round or Equivalent Back Leg Red Meat, 1 kg ',
                    'Bottle of Wine, Mid-Range Price', 'Chicken Breasts, Boneless and Skinless, 1 kg',
                    'Domestic Beer, 0.5 liter Bottle', 'Eggs, 12 pack', 'Lettuce, 1 head',
                    'Loaf of Fresh White Bread, 0.5 kg', 'Local Cheese, 1 kg', 'Milk, Regular,1 liter',
                    'Onion, 1 kg', 'Oranges, 1 kg', 'Pack of Cigarettes', 'Potato, 1 kg', 'White Rice, 1 kg',
                    'Tomato, 1 kg', 'Water, 1.5 liter Bottle', 'One bedroom apartment outside of city centre',
                    'One bedroom apartment in city centre', 'Three bedroom apartment outside of city centre',
                    'Three bedroom apartment in city centre', 'Cappuccino', 'Coca-Cola, 0.33 liter Bottle',
                    'Domestic Beer, 0.5 liter Draught', 'Imported Beer, 0.33 liter Bottle',
                    'McMeal at McDonalds or Alternative Combo Meal',
                    'Meal for 2 People, Mid-range Restaurant, Three-course',
                    'Meal in Inexpensive Restaurant', 'Average Monthly Net Salary, After Tax', 'Cinema ticket, 1 Seat',
                    'Fitness Club, Monthly Fee for 1 Adult', 'Tennis Court Rent, 1 Hour on Weekend',
                    'Gasoline, 1 liter',
                    'Monthly Pass, Regular Price', 'One-way Ticket, Local Transport',
                    'Taxi, price for 1 hour Waiting, Normal Tariff', 'Taxi, price for 1 km, Normal Tariff',
                    'Taxi Start, Normal Tariff', 'Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)',
                    'Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans',
                    'Basic utilities for 85 square meter Apartment including Electricity, Heating or Cooling, Water and Garbage',
                    'Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL', 'Water, 0.33 liter Bottle',
                    'Summer Dress in a Chain Store Like George, H&M, Zara, etc.',
                    'Mortgage Interest Rate in Percentages for 20 Years Fixed-Rate, Yearly, Fixed-Rate',
                    'Imported Beer, 0.33 liter Bottle'])
    currencies = ['BGN', 'EUR', 'USD']
    output_text = 'You have to wait a little for the result calculation\n\n'

    def submit_press(self):
        input_country = self.ids.country_name.text
        input_item = self.ids.item_name.text
        currency_input = self.ids.input_currency.text
        self.ids.output_box.text = country_prices(input_country, input_item, currency_input)

    def country_clicked(self, value):
        self.ids.output_box.text = f'Country: {value}\n\nYou have to wait a little for the result calculation'

    def item_clicked(self, value):
        self.ids.output_box.text = f'Item: {value}\n\nYou have to wait a little for the result calculation'

    def currency_clicked(self, value):
        self.ids.output_box.text = f'Item: {value}\n\nYou have to wait a little for the result calculation'


class WorldPrices(App):
    title = 'Explore World Prices'

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    WorldPrices().run()
