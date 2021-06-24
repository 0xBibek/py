##
## IP.py is provided for educational purpose only.
## Github: 0xbibek
## Twitter: 0xbibek
## Credits to ip-api.com for providing free API.
##

import requests
import json

address = input("Enter IP Address or Domain Name: ")


def ip(address):
	try:
		hscope = requests.get(f"http://ip-api.com/json/{address}")
		data = hscope.json()
		status = data["status"]
		country = data["country"]
		query = data["query"]
		region = data["regionName"]
		city = data["city"]
		isp = data["as"]
		if data["status"] == 'fail':
			output = 'FAILED to catch, Invalid input or Try something else..'
			return output
		else:
			output = f'''
Data: {query}
Status: {status}
Country: {country}
Region: {region}
City: {city}
ISP: {isp}
'''
			return output
	except:
		output = ""
		return output

print(ip(address))