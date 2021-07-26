month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

x, y = map(int,input().split())

d = (sum(month[0:x-1]) + y)%7

print(day[d])

# 추가 공부 코드
# month = [0,31,28,31,30,31,30,31,31,30,31,30,31] #맨 앞에 0을 추가하여 실제 월에 맞게. x-1을 해주지 않아도 됨
# day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
# x, y = map(int,input().split())
# print([(sum(month[:x]) + y)%7-1])