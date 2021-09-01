
#import the required modules
import requests
from bs4 import BeautifulSoup
import json
##list of stocks being used// must be typed out!
mystocks = ['VAST.L', 'ICON.L', 'PREM.L', 'BZT.L','TSLA',]
stockdata = []

#retrieving the data 
def getdata(symbol):
	headers = {'user-agent':''}
	url = f'https://uk.finance.yahoo.com/quote/{symbol}'
	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')
	stock = {
	'symbol':symbol,
	'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
	'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text,
	}
	return stock

##adding the items to other list 
for item in mystocks:
	stockdata.append(getdata(item))
	print('Getting:', item)


print(stockdata)