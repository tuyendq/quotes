# Run this command to read quotes.txt file and generate index.html file
# $ python quotes.py quotes.txt index.html

from sys import argv
import random
import csv

script, file_quotes, file_html = argv

quote_content = ""
quote_author = ""

# Todo: add exception
with open(file_quotes, 'r') as input_file:
	contents = csv.reader(input_file, skipinitialspace=True)

	# Count number of quotes in file
        count = 0
        for row in contents:
                count = count + 1

	# Get a random quote
	random_number = random.randint(1, count)

        # Must rewind input_file to begin: byte 0th
        input_file.seek(0)
        count = 1
        for row in contents:
            if count == random_number:
                #global quote_content
                quote_content = row[0]
                #global quote_author
                quote_author = row[1]
                break
            else:
                count = count + 1

# print "Print to check global variables' values"
# print "Quote content: ", quote_content
# print "Quote author: ", quote_author

def create_html(file_html, quote_content, quote_author):
    """Create a html file with a random quote."""
    # html template
    html_content = """
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset="utf-8">
		<title>What, Why, and How to practice habit?</title>
		<link rel="stylesheet" href="styles.css">
		</head>
		<body>
		<center>
		<blockquote>{quote_content}</blockquote>
		<author>&mdash; {quote_author}</author>
		</center>
		</bofy>
		</html>
		"""
    html_content = html_content.format(quote_content=quote_content, quote_author=quote_author)

    output_file = open(file_html, 'w')
    output_file.write(html_content)
    output_file.close()

# The moment of true: create index.html file with the random quote
create_html(file_html, quote_content, quote_author)
