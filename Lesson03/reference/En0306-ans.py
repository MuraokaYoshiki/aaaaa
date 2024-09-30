#演習５
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

#最低時給
h_wage=np.array([
    889,822,821,853,822,822,828,879,882,865,956,953,1041,1040,
    859,877,861,858,866,877,880,913,955,902,896,937,992,928,866,859,
    821,824,862,899,857,824,848,821,820,870,821,821,821,822,821,821,820
])

#基本統計量
print(f"時給平均 {np.mean(h_wage)}")
print(f"時給標準偏差 {np.std(h_wage)}")
print(f"時給  0％ {np.percentile(h_wage,0)}")
print(f"時給 25％ {np.percentile(h_wage,25)}")
print(f"時給 50％ {np.percentile(h_wage,50)}")
print(f"時給 75％ {np.percentile(h_wage,75)}")
print(f"時給100％ {np.percentile(h_wage,100)}")

#度数分布
BINS=10
dosuu,kaikyuu = np.histogram(h_wage,bins=BINS)

print(f"度数{dosuu}")
print(f"階級{kaikyuu}")

dosuu = np.append(dosuu,0)
#棒グラフ表示
plt.bar(range(BINS+1),dosuu,width=1,tick_label=kaikyuu,align="edge")
#x軸目盛ラベルのフォントサイズを変更する
plt.xticks(fontsize=6)
plt.title("最低時給ヒストグラム")
plt.xlabel("賃金")
plt.ylabel("度数")
plt.savefig("./img/En0306.png")
