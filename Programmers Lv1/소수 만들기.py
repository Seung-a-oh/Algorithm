def solution(nums):
    cnt = 0
    sosu = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                num = nums[i]+nums[j]+nums[k]
                sosu.append(num)

    for _ in sosu:
        for m in range(2,_):
            if _ % m == 0:
                cnt += 1
                break
    return len(sosu)-cnt

print(solution([1,2,3,4]))