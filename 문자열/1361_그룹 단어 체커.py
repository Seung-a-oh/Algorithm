def is_group_word(word):
    counted = []
    while word:
        if word[0] in counted:
            return 0
        counted.append(word[0])
        word = word.lstrip(word[0])
    return 1

res = 0
n = int(input())

for i in range(n):
    word = input()
    res += is_group_word(word)

print(res)