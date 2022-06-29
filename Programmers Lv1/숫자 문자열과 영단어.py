def solution(s):
    dict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
            "eight":8,"nine":9,"ten":10}
    
    for i in dict:
        if i in s:
            s = s.replace(i, str(dict[i]))
    answer = int(s)
    return answer

solution("123")