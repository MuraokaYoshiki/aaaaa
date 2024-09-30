import numpy as np

#2次元配列で作る場合
#15人分の2科目の2次元配列データ
siken = np.random.randint(0,100,(5,2))
print(f"{siken}")
total = np.sum(siken,axis=1)

#totalの配列の体裁を整える
total = total.reshape(-1,1)

#hstackで横方向にスタック(つなげた)
siken = np.hstack((siken,total))
print(f"{siken}")

#縦方向の平均値を計算
avg = np.mean(siken,axis=0)
sd = np.std(siken,axis=0)
print(f"科目ごとの平均{avg}")
print(f"科目ごとの標準偏差{sd}")

#行列のスライス :はすべて ,2は2列目
print(f"合計点だけを表示{siken[:,2]}")

#偏差値 2は2列目ということ
hensati = 10 * (siken[:,2] - avg[2]) / sd[2] + 50
print(f"合計点の偏差値{np.round(hensati,1)}")

siken = np.hstack((siken,hensati.reshape(-1,1)))

print(f"3科目の合計点、合計点の偏差値 \n {siken}")