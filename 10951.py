while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# list=[]
# count=0
# while True:
#     try:
#         a, b = map(int, input().split())
#         list.append(a+b)
#         count += 1
#     except:
#         for i in range(count):
#             print(list[i])
#         break