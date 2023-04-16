def check_group(word):
    alpha = []
    i = 0
    while i < len(word):
        if word[i] in alpha:
            return False
        alpha.append(word[i])
        temp = word[i]
        while temp == word[i]:
            i += 1
            if len(word) == i:
                break
    return True
        
word_num = int(input())
words = []
for i in range(word_num):
    words.append(input().strip())
print(len(tuple(filter(check_group, words))))