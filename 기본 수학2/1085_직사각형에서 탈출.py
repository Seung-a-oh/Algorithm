x,y,w,h = map(int, input().split())

if w-x <= x:
    a = w-x
else:
    a = x

if h-y <= y:
    b = h-y
else:
    b = y

if a <= b:
    print(a)
else:
    print(b)

    
# 코드 추가 공부
# x, y, w, h = map(int,input().split())
# k = min(x, w-x, h-y, y)
# print(k)