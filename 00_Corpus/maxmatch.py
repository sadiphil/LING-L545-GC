import sys

def maxmatch(dictionary, line):
	dictionary = [(len(line), line.strip()) for line in open(sys.argv[1]).readlines()]
	dictionary.sort()
	dictionary.reverse()

	return line
dictionary = []

line = sys.stdin.readline()

while line:
	print(maxmatch(dictionary, line.strip('\n')))

	line = sys.stdin.readline()
