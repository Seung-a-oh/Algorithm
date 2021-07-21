str = input()
for i in range(len(str)):
    if i%10 == 0:
        print(str[i:i+10])