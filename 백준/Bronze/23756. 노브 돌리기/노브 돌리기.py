nob_num = int(input()) + 1

A = []
for i in range(nob_num):
	A.append(int(input()))
total = 0
for i in range(nob_num - 1):
	cha = abs(A[i+1]-A[i])
	if cha < 180:
		total += cha
	else:
		total += 360 - cha

print(total)