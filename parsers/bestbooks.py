from os.path import abspath, dirname, join as pathjoin

def get():
	books = []

	filename = 'bestbooks.txt'

	# Apparently you can't just open file by relative path in submodule
	filepath = pathjoin(dirname(abspath(__file__)), filename)

	f = open(filepath)
	lines = f.readlines()

	for line in lines:
		line = line.strip()

		# Get rid of numbers
		line_author_name = line.split('.')[1]
		data = line_author_name.split('-')
		author, name = data[0], ''.join(data[1:])
		author = author.strip()
		name = name.strip()

		books.append((author, name))
		
	return books

