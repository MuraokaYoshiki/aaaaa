import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from mydblib2 import my_select

print("【T122142】 小問番号2")

# SQLの設定
sqlstring = f"""
    SELECT * FROM iris;
"""

#webtest データベースの iris テーブルのレコードを読み込み
iris = my_select("wptest", sqlstring)

#print(iris)
mean = iris.groupby("kinds").mean(numeric_only=True)
std = iris.groupby("kinds").std(numeric_only=True)
print(f"平均値\n{mean}")
print()
print(f"標準偏差\n{std}")

mean_pl = mean["petallength"]

sqlstring = f"""
    SELECT COUNT(*) FROM iris;
"""
n = int(my_select("wptest", sqlstring).values)

#棒グラフ表示
plt.bar(range(len(mean_pl)), mean_pl, width=0.8, tick_label=["setoa", "versicolor", "viriginica"])
plt.xticks(fontsize=6.0)
plt.title(f"petallength n={n}")
plt.xlabel("kinds")
plt.ylabel("mm")
plt.savefig("./TS1-T122142-2.png")