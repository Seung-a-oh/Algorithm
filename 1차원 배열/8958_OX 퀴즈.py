import sys 

for _ in range(int(input())):
    a = list(sys.stdin.readline().rstrip())
    check = 0
    score = 0
    for i in a:
        if i == "O":      
            check += 1
            score += check
        else:
            check = 0
    print(score)