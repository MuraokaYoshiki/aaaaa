import numpy as np
th = 75/180*np.pi
r = 5
c = 2 * r * np.sin(th/2)
L = r * th

print(f"c={c:.3f} L={L:.3f} ")