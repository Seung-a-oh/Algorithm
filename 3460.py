for i in range(int(input())):
    num = list(bin(int(input())))
    num.reverse()

    for i in range(len(num)):
        if(num[i]=="1"):
            print(i, end=" ")