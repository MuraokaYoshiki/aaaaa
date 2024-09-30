#例題７　numpyモジュール　
import numpy as np   #numpyモジュールを呼び出し　npとして利用する

#10個の一様乱数 data1 を生成
data1 = np.random.rand(10)
print( data1 )

#10個の0～100までの一様乱数を生成
data2 = np.random.randint(0,100,10)
print( data2 )

