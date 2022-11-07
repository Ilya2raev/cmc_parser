import json
import requests
from coins import coins
from lxml import etree
import lxml.html
from urls import url

def parse(url):
	dict = {}
	count = 0
	try:
		response = requests.get(url)
		print(f'[Status Code {response.status_code}]')
		tree = lxml.html.document_fromstring(response.text)
		token = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr/td[3]/div/a/div/div/div/p/text()')
		price = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr/td[4]/div/a/span/text()')

		for i in token:
			dict[i] = price[count]
			count += 1
		with open('tokens.json', 'w') as token_file:
			json.dump(dict, token_file, indent=4, sort_keys=True)

		with open('coins.json', 'w') as file:
			json.dump(coins, file, indent=4, sort_keys=True)
		print('[Data writing successful]')

	except:
		print('[An error occured. Try again later]')

def main():
	parse(url)

if __name__ == '__main__':
	main()