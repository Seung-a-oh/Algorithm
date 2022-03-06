n = int(input())
liquid = list(map(int, input().split()))

dict = {}
for a in liquid:
    for b in liquid[liquid.index(a)+1:]:
        for c in liquid[liquid.index(b)+1:]:
            dict[a,b,c] = abs(a+b+c)

min_list = [list(k) for k,v in dict.items() if min(dict.values()) == v]
min_list = min_list[0]
min_list.sort()
print(min_list[0],min_list[1],min_list[2])

# from itertools import combinations
#
# combi = list(combinations(liquid,3))
# b = abs(sum(combi[0]))
# answer = combi[0]

# for _ in combi:
#     if b > abs(sum(_)):
#         b = abs(sum(_))
#         answer = list(_)
        
# answer.sort()
# print(answer[0],answer[1],answer[2])