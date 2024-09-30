import numpy as np

#1次元配列で作る場合
#15人分の数学の試験の点数
suugaku = np.random.randint(0,100,15)
#15人分の英語の試験の点数
eigo = np.random.randint(0,100,15)#0以上100未満のデータが15個
total = suugaku + eigo
#合計の平均値
avg_total = np.mean(total)
#合計の標準偏差
std_total = np.std(total)
#偏差値の計算
hensati = 10 * (total - avg_total)/std_total + 50

print(f"数学:{suugaku}")
print(f"英語:{eigo}")
print(f"合計:{total}")
print(f"偏差値:{np.round(hensati,1)}")