num = int(input())
hansu = 0

for n in range(1, num+1):
    if n <= 99:
        hansu += 1
    else:     
        n = str(n)
        if int(n[0])-int(n[1]) == int(n[1])-int(n[2]):
            hansu+=1
print(hansu)

# 추가
# nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1