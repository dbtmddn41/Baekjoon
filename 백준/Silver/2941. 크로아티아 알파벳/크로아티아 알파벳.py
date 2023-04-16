ori_str = input()
leng = len(ori_str)
size = leng
for i in range(1, size):
    if ori_str[i] == '=' or ori_str[i] == '-':
        leng -= 1
        if ori_str[i-1] == 'z' and i > 1:
            if ori_str[i-2] == 'd':
                leng -= 1
    elif ori_str[i] == 'j':
        if ori_str[i-1] == 'l' or ori_str[i-1] =='n':
            leng -= 1
print(leng)