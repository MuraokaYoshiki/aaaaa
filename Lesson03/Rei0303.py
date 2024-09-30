#例題３
import numpy as np
import matplotlib.pyplot as plt

#身長と体重のベクトルデータを正規乱数で作成
sintyou = np.array( [169,164,161,169,177,166,170,163,157,166,171,162,165,
    161,166,161,168,165,158,168,164,168,170,161,158,170,170,154,158,
    162,160,163,154,165,162,170,167,162,168,160] )
taijyuu = np.array( [75,75,68,73,63,57,65,60,62,67,65,60,68,64,62,67,
    72,63,50,57,51,70,68,57,59,62,57,54,58,54,55,65,50,67,71,70,
    58,56,58,70]) 
#print( f"身長 {sintyou}")    #for debug
#print( f"体重 {taijyuu}")    #for debug

#相関行列(Correlation Matrix) cm を求める
cm = np.corrcoef(sintyou,taijyuu)
print(f"相関行列 \n {cm}")
#相関行列の0行1列から相関係数ｒを代入
#r = cm[0,1] 

#回帰直線の傾きaと切片ｂを計算
#a,b = np.polyfit( sintyou ,taijyuu,1)
#回帰直線の方程式を表示
#print(f"回帰直線の方程式は y = {a}x + {b}")
#回帰直線の座標データを作成
#xの値は，x軸の最小値と最大値
#x = np.array([np.min(sintyou),np.max(sintyou)])
#ｙの値は，回帰直線に合わせて算出
#y = a * x + b
#print(f"x = {x}")  #for debug
#print(f"y = {y}") #for debug

#グラフタイトルに相関係数を表示する
#plt.title(f"Scatter r={r}")
#x軸とy軸のラベルを設定する
plt.xlabel("height" )
plt.ylabel("weight" )
#散布図のパラメータを設定する
plt.scatter( sintyou , taijyuu, color="r" )
#回帰直線のグラフ表示
#plt.plot(x,y,label=f"y={a}x+{b}")
#グラフ表示/出力
#plt.legend()
plt.savefig("./img/Rei0303.png")
plt.close()
