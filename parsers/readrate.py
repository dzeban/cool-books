from bs4 import BeautifulSoup
from requests import request

def get():
	link = 'http://readrate.com/rus/ratings/top100'

	soup = BeautifulSoup(request('GET', link).text)
	items = soup.select('.item-book')

	books = []
	for item in items:
		title = item.select('h3.title')[0].text
		author = item.select('li.contributor')[0].text
		books.append((author, title))

	return books

