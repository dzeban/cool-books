#!/usr/bin/env python3

from collections import OrderedDict

class Book:
	author = ''
	title = ''
	def __init__(self, author, title):
		self.author = author
		self.title = title


class Library:
	# Key is a title
	# Value is dict of book object and count
	_lib = {}

	def add(self, book):
		b = self._lib.get(book.title)
		if b is None:
			self._lib[book.title] = {'book': book, 'count': 1}
		else:
			b['count'] += 1
	
	def sorted(self):
		return OrderedDict(sorted(
			self._lib.items(), 
			key = lambda b: b[1]['count'], 
			reverse = True))

