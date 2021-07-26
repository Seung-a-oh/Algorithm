TestCase = int(input())

NumArray = [int(x) for x in input().split()]

NumArray.sort()
print(NumArray[0], NumArray[TestCase-1])


#추가 공부 코드
# TestCase = int(input())
#
# NumArray = [int(x) for x in input().split()]
#
# print(min(NumArray), max(NumArray))