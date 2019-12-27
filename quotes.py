# Run this command to read quotes.txt file and generate index.html file
# $ python quotes.py quotes.txt index.html

from sys import argv
import sys
import random
import csv

# Todo: Check number of arguments and print usage syntax
while True:
    if (len(argv) != 3):
        print "Usage: python quotes.py quotes.txt index.html"
        sys.exit(1)
    else:
        break

script, file_quotes, file_html = argv

quote_content = ""
quote_author = ""
bgcolors = ["00BA51","3B5998","1F70C1","A3AAAE","FF9900"]
bgcolor = random.choice(bgcolors)

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
                quote_content = row[0]
                quote_author = row[1]
                break
            else:
                count = count + 1

def create_html(file_html, quote_content, quote_author):
    """Create a html file with a random quote."""
    # html template
    html_content = """
		<!DOCTYPE html>
		<html amp lang="en">
		<head>
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
        <meta name="description" content="Practice Habits: Hour of Quote"/>
        <link rel="canonical" href="https://www.practicehabits.net/">
		<title>What, Why, and How to practice habit?</title>

        <script async src="https://cdn.ampproject.org/v0.js"></script>

		<style amp-custom>
            body {{background-color: #{bg_color}; font-size: 1rem;}}
            blockquote {{color: #FFFFFF; font-size: 3rem; border-style: solid; padding: 1rem;}}
            .author {{font-size: 2rem; font-style: italic;}}
        </style>
        <style amp-boilerplate>body{{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}}@-webkit-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-moz-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-ms-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-o-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}</style><noscript><style amp-boilerplate>body{{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}}</style></noscript>
		</head>
		<body>
		<center>
		<blockquote>{quote_content}</blockquote>
		<p class="author">&mdash; {quote_author}</p>
		</center>
		</bofy>
		</html>
		"""
    html_content = html_content.format(bg_color=bgcolor, quote_content=quote_content, quote_author=quote_author)

    output_file = open(file_html, 'w')
    output_file.write(html_content)
    output_file.close()

# The moment of true: create index.html file with the random quote
create_html(file_html, quote_content, quote_author)
