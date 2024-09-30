#例題８
#form モジュール名 import メソッド名 表記
import numpy as np
from numpy.random import randint

#サイコロを100回投げた結果をsaikoroに代入する
#saikoro = np.random.randint(1,6,100)
#randintメソッドをインポート済みのためメソッド名のみで利用できる
saikoro = randint(1,6,100)
print(saikoro) #for debug

avg = np.mean( saikoro )
st = np.std( saikoro )
print(f"平均={avg}  標準偏差={st}")