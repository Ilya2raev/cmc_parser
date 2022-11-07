import requests
from lxml import etree
import lxml.html
from urls import url


def parse(url):
	dict = {}
	count = 0
	try:
		# global token, price       			for experiments
		response = requests.get(url)
		tree = lxml.html.document_fromstring(response.text)
		token = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr/td[3]/div/a/div/div/p/text()')
		price = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr/td[4]/div/a/span/text()')

		for i in token:
			dict[i] = price[count]
			count += 1
		return dict
	except:
		print('An error occured. Try again later')

def main():
	print(parse(url))

if __name__ == '__main__':
	main()
	



#experiments with data

# new_price = []
# for i in price:
# 	a = i.replace(',', '')
# 	new_price.append(round((float(a[1:])+1000), 2)) #добавляет в список цену без знака $ c точностью 2 знака

# new_token = []
# counter1 = 1
# for r in token:
# 	r = f'Coin{counter1}'
# 	new_token.append(r)
# 	counter1 += 1

# def false_price(list1, list2):
# 	dict = {}
# 	counter2 = 0
# 	for t in new_token:
# 		dict[t] = new_price[counter2]
# 		counter2 += 1
# 	print(dict)

# false_price(new_token, new_price)