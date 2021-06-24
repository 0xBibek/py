##
## Github: 0xbibek
## Credits to meme-api.herokuapp.com
##

import requests
import json

def meme():
	memeget = requests.get('https://meme-api.herokuapp.com/gimme')
	memeSent = memeget.json()['url']
	memeMsg = '' + memeSent
	return memeMsg

print(meme())