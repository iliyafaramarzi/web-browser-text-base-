from googlesearch import search
from tabulate import tabulate
import urllib.request
import webbrowser

inp = input('>> ')
searchs = []
stat = 0

for search in search(inp, num_results=100):
	searchs.append(search)
	
print(tabulate({'resualts' : searchs[stat:stat + 10]}, headers = 'keys', tablefmt = 'fancy_grid', showindex="always"))



while True:	
	try:
		inp = input('>> ')
		
		li = inp.split(' ')
		
		if inp == '>':
			stat += 10
			print(tabulate({'resualts' : searchs[stat : stat + 10]}, headers = 'keys', tablefmt = 'fancy_grid', showindex="always"))
			
		elif inp == '<':
			if stat != 0:
				stat -= 10
			print(tabulate({'resualts' : searchs[stat : stat + 10]}, headers = 'keys', tablefmt = 'fancy_grid', showindex="always"))
		
		elif inp == 'page':
			print(stat / 10)
			
		elif li[0] == 'open':
			webbrowser.open(searchs[stat + int(li[1])]) 

		elif li[0] == 'ping':
			status_code = urllib.request.urlopen(searchs[stat + int(li[1])]).getcode()
			if status_code == 200 : print('Online')
			else : print('Offline')
			
	
		
	
	except IndexError:
		print("Invalid index!")
	

