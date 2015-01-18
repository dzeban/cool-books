#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import request

def get():
	link_wiki = 'https://ru.wikipedia.org/wiki/100_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D0%BA%D0%BD%D0%B8%D0%B3_%D0%B2%D1%81%D0%B5%D1%85_%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD_%D0%B8_%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BE%D0%B2'

	soup = BeautifulSoup(request('GET', link_wiki).text)

	table = soup.select('table.wikitable')[0]

	books = []
	for tr in table.findAll('tr')[1:]:
		tds = tr.findAll('td')
		title = tds[0].text
		author = tds[1].text
		books.append((author, title))
	
	return books
