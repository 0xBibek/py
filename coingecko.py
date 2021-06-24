##
## Github: 0xbibek
## Credits to coingecko.com
##

import requests
import json

name = input("Name of CryptoCurrency: ")

def coingecko(name):
	try:
		crypto = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols={name}")
		data = crypto.json()
		cryptoPrice = data[0]["current_price"]
		cryptoRank = data[0]["market_cap_rank"]
		cryptoChanges = data[0]["price_change_percentage_24h"]
		cryptoCap = data[0]["market_cap"]
		cryptoName = data[0]["name"]
		cryptoSymbol = data[0]["symbol"]


		output = f'''
Rank:  #{cryptoRank}
{cryptoSymbol} ({cryptoName}):  ${cryptoPrice}
Changes (24hr):  {cryptoChanges}%
Market Cap:  ${cryptoCap}
			'''
		return output
	except:
		output = ""
		return output

print(coingecko(name))