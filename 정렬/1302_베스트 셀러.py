T = int(input())
array = []

for _ in range(T):
    array.append(input())

set_array = set(array)
num = {}
for i in set_array:
    num[i] = array.count(i)

max_list = [k for k,v in num.items() if max(num.values()) == v]
max_list.sort()
print(max_list[0])
