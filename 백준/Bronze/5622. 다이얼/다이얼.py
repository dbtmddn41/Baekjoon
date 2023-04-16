def make_num(c):
    if c < 'S':
        return (ord(c)-65)//3+2
    if c == 'Z':
        return 9
    return (ord(c)-66)//3+2

phone = input()
total = 0
for x in phone:
    total += make_num(x)+1
print(total)