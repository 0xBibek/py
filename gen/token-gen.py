##
## Github: 0xbibek
## Twitter: 0xbibek
##

import secrets
import string

def tokenGen():
	ranToken = secrets.token_hex(32)
	tokenn = 'Random Token: ' + ranToken
	return tokenn


print(tokenGen())