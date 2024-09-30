import numpy as np

#1列目はすべて1で良い
#行は1段ずつ1行増えていく
#1 2  3  4  5   6   7  8 9 10
#↓ ↓  ↓  ↓  ↓   ↓   ↓  ↓ ↓  ↓
#1 ↓  ↓  ↓  ↓   ↓   ↓  ↓ ↓  ↓
#1 1  ↓  ↓  ↓   ↓   ↓  ↓ ↓  ↓
#1 2  1  ↓  ↓   ↓   ↓  ↓ ↓  ↓
#1 3  3  1  ↓   ↓   ↓  ↓ ↓  ↓
#1 4  6  4   1  ↓   ↓  ↓ ↓  ↓
#1 5 10 10   5   1  ↓  ↓ ↓  ↓
#1 6 15 20  15   6  1  ↓ ↓  ↓
#1 7 21 35  35  21  7  1 ↓  ↓
#1 8 28 56  70  56 28  8 1  ↓
#1 9 36 84 126 126 84 36 9  1

ndarray=np.zeros((10, 10), dtype=int)
ndarray[:,0]=1

for i in range(1,10):
    for j in range(1,i+1):
        ndarray[i][j]=ndarray[i-1][j-1]+ndarray[i-1][j]

for i in range(10):
    for j in range(0, i + 1):
        print(f"{ndarray[i][j]}", end=" ")
    print()