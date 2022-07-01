def solution(s):
    slen = len(s)

    if slen == 1:
            return 1

    temp = "";    now = ""
    answer = 1000

    for i in range(1, slen//2+1):
        count = 1;
        leng = 0;
        temp = s[0:i]

        for j in range(i,slen,i):
            now = s[j:j+i]
            if temp == now:
                count += 1
            else:
                if count > 1:
                    leng += i+len(str(count))
                else:
                    leng += i
                count = 1
            temp = now
        if count > 1:
            if answer > leng+len(temp)+len(str(count)):
                answer = leng+len(temp)+len(str(count))
        else:
            if answer > leng+len(temp):
                answer = leng+len(temp)

    return answer

print(solution("ababcdcdababcdcd"))
