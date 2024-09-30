import numpy as np

for cnt in range(100,1001,100):
    #3つのサイコロを100回投げる
    saikoro = np.random.randint(1,7,(cnt,3))
    #3つのサイコロの和
    total = np.sum(saikoro,axis=1)
    avg = np.mean(total)
    sd = np.std(total)
    print(f"試行回数{cnt}回 平均値{avg:.3f} 標準偏差{sd:.3f}")

