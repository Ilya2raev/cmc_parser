import requests
from coins import coins

for pic in coins.values():
	res = requests.get(f'https://s2.coinmarketcap.com/static/img/coins/64x64/{pic}')

	with open(pic, 'wb') as file:
		file.write(res.content)