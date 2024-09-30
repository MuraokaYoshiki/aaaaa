import numpy as np
a,b,c=5,6,8
s=(a+b+c)/2
S=np.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"面積は{S:.3f}")