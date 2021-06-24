##
## Github: 0xbibek
## Credits to quotable.io
##

import requests
import json

def quotes():
	quote = requests.get('https://api.quotable.io/random')
	quoteContent = quote.json()['content']
	quoteAuthor = quote.json()['author']
	quoteMsg = '' + quoteContent + ' - ' + quoteAuthor
	return quoteMsg

print(quotes())