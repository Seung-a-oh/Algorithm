S = input()

al = [-1]*26
count = 0
for _ in S:
    a = ord(_)-97
    if al[a]==-1:
        al[a]=count
    count+=1

print(" ".join(str(i) for i in al))

