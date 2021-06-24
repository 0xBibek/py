##
## Github: 0xbibek
## Twitter: 0xbibek
## Credits will be appreciated. :D
##

import requests
import bs4 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Rashifal Lists:\n")
print(" | Singha | Brish | Mithun | Mesh | Kanya | Karkat |")
print(" | Tula | Kumbha | Dhanu | Makar | Min | Brish |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


name = input("Tapaiko rashifal?: ")

def rashifal(name):
	try:
		rashi = requests.get(f"https://www.hamropatro.com/rashifal/daily/{name}")
		khojiyo = bs4.BeautifulSoup(rashi.text, "html.parser")
		kun = khojiyo.find_all('p')[0].find_all(text=True, recursive=True)
		rashidata = ''.join([str(elem) for elem in kun])
		output = f'''
Rashifal: {rashidata}
	'''
		return output
	except:
		output = 'Error Occured.'
		return output

print(rashifal(name))