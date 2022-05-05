cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
alpha = input() 

for c in cro: 
    alpha = alpha.replace(c, 'c') 

print(len(alpha))
