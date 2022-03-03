S = input()

array = []
for _ in range(len(S)):
    a = S[_:]
    array.append(a)
array.sort()

for _ in array:
    print(_)