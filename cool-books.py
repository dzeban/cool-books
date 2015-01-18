#!/usr/bin/env python3

from book import Book, Library

import parsers.wiki100

L = Library()

wiki100 = parsers.wiki100.get()

for el in wiki100:
	book = Book(el[0], el[1])
	L.add(book)

d = L.sorted()

for k,v in d.items():
	print('{} : {}'.format(k,v['count']))
