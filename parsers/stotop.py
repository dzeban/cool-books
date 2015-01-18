from bs4 import BeautifulSoup
from requests import request

def get():
	link = 'http://stotop.com/top/100_luchshih_knig/'

	soup = BeautifulSoup(request('GET', link).text)
	items = soup.select('.element_name_container')

	books = []

	for item in items:
		parts = item.text.split(',')
		
		try:
			title = parts[0].split('.')[1].strip()
			author = parts[1].strip()
		except IndexError: # У приключений Гулливера нет автора *facepalm*
			author = ''

		books.append((author, title))

	return books
