#例題８
import numpy as np

#サイコロを100回投げた結果をsaikoroに代入する
saikoro = np.random.randint(1,6,[3,5])
print(saikoro) #for debug
#axis=1で行の何かを求められる
#axis=0で列の何かを求められる
#↓の場合は平均値np.meanだから
avg = np.mean( saikoro , axis=1)
st = np.std( saikoro )
print(f"平均={avg}  標準偏差={st}")