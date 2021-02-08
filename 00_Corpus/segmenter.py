import sys, re

line = sys.stdin.readline ()
while line != ' ':
	for token in line.split (' '):
		if token.strip() == '':
			continue
		if token[-1] in '!?;':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':
			if token in ['etc.', '.,', ',  .', ', .', 'Mlle', 'Mdme.', 'i.e.', 'kg.', 'e.g.', ':', '...', ',', ':  ,', '. ,']:
				sys.stdout.write(token + ' ')
			elif re.findall('[0-9]+\.', token):
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline ()
