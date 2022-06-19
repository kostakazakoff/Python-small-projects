import requests

url = "https://cost-of-living-and-prices.p.rapidapi.com/cities"

headers = {
	"X-RapidAPI-Key": "d7b2cfb21emsh20a00fb247fdfcbp19dd36jsn724c6d53f092",
	"X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = response.json()
cities = data['cities']
countries = sorted(set([cities[i]["country_name"] for i in range(len(cities))]))
print(countries)

# print(response.text)
# with open('d:/cities.txt', 'w') as f:
# 	info = str(response.text)
# 	f.write(info)

# countries = [data[i]["country_name"] for i in range(len(data))]
# print(countries)