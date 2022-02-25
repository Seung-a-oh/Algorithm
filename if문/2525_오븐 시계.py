hour, minute = map(int, input().split())
time = int(input())

h = time // 60
m = time % 60

hour = hour + h
minute = minute + m

if minute >= 60:
    if minute == 60:
        minute = 0
    else:
        minute -= 60
    hour +=1

if hour >= 24:
    hour %= 24 
print(hour, minute)