import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    li = []  
    
    for S in Stars:
        li.append(S*3)
    for S in Stars:
        li.append(S+' '*(LEN//3)+S)
    for S in Stars:
        li.append(S*3)
    return li

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))