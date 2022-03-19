# 1차 코드 - 시간 초과
# import sys
# N = int(sys.stdin.readline())
# array = []

# for _ in range(N):
#     array.append(int(input()))

# print(round(sum(array)/N))

# array.sort()
# print(array[N//2])

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

# print(max(array)-min(array))


# 2차 코드 - 시간 초과
# import sys
# N = int(sys.stdin.readline())
# array = []

# for _ in range(N):
#     array.append(int(input()))

# print(round(sum(array)/N))

# array.sort()
# print(array[N//2])

# dict = {}
# for _ in array:
#     dict[_] = array.count(_)
# max_list = [k for k,v in dict.items() if max(dict.values()) == v]
# max_list.sort()
# if len(max_list) > 1:
#     print(max_list[1])
# else:
#     print(max_list[0])

# print(max(array)-min(array))

# 3차 코드
import sys
from collections import Counter

N = int(sys.stdin.readline())
array = []

for _ in range(N):
    array.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(array)/N))

# 중앙값
array.sort()
print(array[N//2])

# 최빈값
# array에서 값 별 횟수를 세어서 저장해준다.
# 횟수를 기준으로 내림차순으로 정렬되고, 동일 횟수에서는 값을 기준으로 오름차순 정렬된다.
common = Counter(array).most_common()
# 값이 하나 이상이고, 최빈값이 두 개 이상일 경우
if len(common) > 1 and common[0][1] == common[1][1]:
    # 두번째 최빈값의 값을 출력하고
    print(common[1][0])
else:
    # 최빈값이 하나일 경우 최빈값의 값을 출력한다.
    print(common[0][0])

# 범위
print(max(array)-min(array))
