#復習問題１

import numpy as np
#15人×3科目の試験結果を乱数で入力
siken = np.random.randint(0,101,(15,3))
#print(f"{siken}")

#15人それぞれの3科目の合計点を計算
#goukei = np.sum(siken)#これだと45個全体の合計になっちゃう
goukei = np.sum(siken,axis=1)#これで横方向の和を計算する！
#print(f"{goukei}")

#平均値と標準偏差を計算
ave = np.mean(goukei)
std = np.std(goukei)
print(f"合計点の平均値{ave:.1f} 標準偏差{std:.1f}")#「:.1f」で小数第1位まで


#偏差値を計算→偏差値=(各人の合計点-平均)/標準偏差×10+50
hensati = np.round((goukei-ave)/std*10+50,1)#np.roundをつけて、最後に「,1」をつければ、小数第1位までになる
#print(f"偏差値{hensati}")

#結果を配列のように出力
result = np.hstack((siken , goukei.reshape(-1,1)))#hstackとかは()が2ついる！！
result = np.hstack((result , hensati.reshape(-1,1)))
print("  数学  国語  英語 合計点 偏差値")
print(result)

#度数分布を作る
hist ,bin_edge = np.histogram(goukei,bins=10,range=(0,300))
print(f"度数分布表:{hist}")
print(f"階級の値:{bin_edge}")

#相関係数
co = np.round(np.corrcoef(siken,rowvar=False),3)#列方向のデータはFalse
print(f"科目ごとの相関行列\n{co}")