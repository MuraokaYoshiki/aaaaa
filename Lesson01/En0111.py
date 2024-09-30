import numpy as np

cnt=300
#3つのサイコロを100回投げる
saikoro = np.random.randint(1,7,(cnt,2))
#3つのサイコロの和
total = np.sum(saikoro,axis=1)
avg = np.mean(total)
sd = np.std(total)
med = np.median(total)
print(f"試行回数{cnt}回 平均値{avg:.3f} 標準偏差{sd:.3f} 中央値{med}")
print(total)
hist = np.histogram(total,bins=11,range=(2,13))
print(f"histgram = {hist}")