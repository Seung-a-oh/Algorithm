N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

print(round(sum(array)/N))

array.sort()
print(array[N//2])

dict = {}
for _ in array:
    dict[_] = array.count(_)
max_list = [k for k,v in dict.items() if max(dict.values()) == v]
max_list.sort()
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])

print(max(array)-min(array))

# 최빈값 - 시간 초과
# dict = {}
# for _ in array:
#     dict[_] = array.count(_)
# sorted_dict = sorted(dict.items(),key = lambda item: item[1], reverse=True)

# if len(sorted_dict) <= 1:
#     print(array[0])
# elif sorted_dict[0][1] == sorted_dict[1][1]:
#     print(sorted_dict[1][0])
# else:
#     print(sorted_dict[0][0])