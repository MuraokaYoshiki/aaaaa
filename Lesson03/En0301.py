import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    y = 1/(1+ np.exp(-x))
    return y

#xの値を設定
x = np.linspace(-5,5,100)
#def sigmoidを呼び出して、yの値を計算
y = sigmoid(x)

#グラフを作成するプログラム

