sosu = [1,2]
n = 2
d = 0

for i in range(2,1001):

    for j in range(1,n):
    
        temp = sosu[j]
        if(i % temp == 0):
        
            d = 1
            break

    if(d == 0):
        sosu.append(i)
        n+=1
    else:
        d = 0
    
for j in range(0,n):

    temp = sosu[j]
    if(temp != 1):
        print(f"{temp}\n")
