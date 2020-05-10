import random
def random_line(fname):
    try:
        lines = open(fname).read().splitlines()
        return random.choice(lines)
    except IOError:
        print("An exception occurred while open file: " + fname)

line = random_line('colors.txt')
if (line != None):
    print(line)
line = random_line('quotes.txt')
if (line != None):
    print(line)