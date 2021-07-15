assocs = []

tot = []

with open('assoc.txt', 'r') as f:
	for line in f.readlines():
		sp = line.strip().split(' ', 1)
		sp[1] = sp[1].split(',')
		without_spaces = []
		for el in sp[1]:
			without_spaces.extend(el.split(' '))
		sp[1] = without_spaces
		assocs.append(sp)
		
def process(text):
	text = text.split(' ')
	matches = {'general'}
	for type in assocs:
		for token in type[1]:
			if token in text:
				matches.add(type[0])
	return matches
	
while True:
	line = input()
	print(process(line))
	
