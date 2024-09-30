import numpy as np
a0=0
a1=1
print(f"1項は、{a1}")
for i in range(2,11):
    a2=a1+a0
    print(f"{i}項は、{a2}")
    a0=a1
    a1=a2