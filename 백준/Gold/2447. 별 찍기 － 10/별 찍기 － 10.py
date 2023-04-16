def make_blank(n):
	if n == 3:
		return ['   ']*3
	blanks = []
	for i in range(9):
		blanks += [make_blank(n//3)]
	return blanks

def make_star(n):
	if n == 3:
		return ['***','* *','***']
	stars = [[]]*9
	for i in range(9):
		if i == 4:
			stars[i] = make_blank(n//3)
		else:
			stars[i] = make_star(n//3)
	return stars

def print_star_line(stars):
	if isinstance(stars[0][0], str):
		print(stars[0][0],stars[1][0],stars[2][0],sep='',end='')
		for x in range(3):
			stars[x].pop(0)
		for x in range(3):
			if not stars[0]:
				del stars[0]
	else:
		for y in range(3):
			print_star_line(stars[y])
		for x in range(3):
			if not stars[0]:
				stars.pop(0)
			

def print_star(stars, n):
	for i in range(n):
		print_star_line(stars)
		print()

n = int(input())
if n == 3:
	print("***\n* *\n***")
else:
	print_star(make_star(n), n)