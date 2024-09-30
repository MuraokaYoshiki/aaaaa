#例題３
import numpy as np
import matplotlib.pyplot as plt

#身長と体重のベクトルデータを正規乱数で作成
h_wage = np.array( [879,882,865,956,953,1041,1040,859,877,861,858,866,877])
p_density = np.array( [478.4,308.1,310.1,1913.4,1206.5,6168.7,3777.7,183.1,251,275.7,187.7,187,154.8] )
#print( f"身長 {sintyou}")    #for debug
#print( f"体重 {taijyuu}")    #for debug

#相関行列(Correlation Matrix) cm を求める
cm = np.corrcoef(h_wage,p_density)
print(f"相関行列 \n {cm}")
#相関行列の0行1列から相関係数をｒを代入
r = cm[0,1] 

#回帰直線の傾きaと切片ｂを計算
a,b,c = np.polyfit( h_wage ,p_density,2)
#回帰直線の方程式を表示
print(f"回帰曲線の方程式は y = {a}x**2 + {b}*x + {c}")
#回帰直線の座標データを作成
#xの値は，x軸の最小値と最大値
x = np.linspace(np.min(h_wage),np.max(h_wage),20)
#ｙの値は，回帰直線に合わせて算出
y = a * x**2 + b *x + c
print(f"x = {x}")  #for debug
print(f"y = {y}") #for debug

#グラフタイトルに相関係数を表示する
plt.title(f"Scatter r={r:.3f}")
#x軸とy軸のラベルを設定する
plt.xlabel("h_wage" )
plt.ylabel("p_density" )
#散布図のパラメータを設定する
plt.scatter( h_wage , p_density, color="r" )
#回帰直線のグラフ表示
plt.plot(x,y,label=f"y={a:.3f}x**2+{b:.3f}x+{c:.3f}")
#グラフ表示/出力
#plt.show()
plt.legend()
plt.savefig("./img/En0304.png")
plt.close()

