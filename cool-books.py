#!/usr/bin/env python3

from book import Book, Library

import parsers.bestbooks
import parsers.readrate
import parsers.stotop
import parsers.wiki100

L = Library()

ratings = []
ratings.append(parsers.wiki100.get())
ratings.append(parsers.bestbooks.get())
ratings.append(parsers.readrate.get())
ratings.append(parsers.stotop.get())

for rating in ratings:
	for el in rating:
		book = Book(el[0], el[1])
		L.add(book)

d = L.sorted()

for k,v in d.items():
	print('{}, {} : {}'.format(k, v['book'].author, v['count']))
