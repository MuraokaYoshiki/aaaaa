import numpy as np
a=np.random.randint(2,10)
b=np.random.randint(2,10)
c=np.random.randint(2,10)
s=(a+b+c)/2
S=np.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"a={a},b={b},c={c}")

if(S<=0):
    print("三角形なし")
else:
    print(f"面積は{S:.3f}")