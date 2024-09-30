import numpy as np
import random

#距離の設定
#2000mから5000mの100mずつ
kyori = random.randrange(1000,5000,100)
#kyori=1000

for kyori in range(1000,10001,500):
    
    if(kyori<=1500):
        hiru_ryoukin = 710
    #if文の終わり
    else:
        #区間
        kukan = np.ceil((kyori-1500)/283)
        #昼間の料金
        hiru_ryoukin = 710+kukan*90
    #夜間の料金
    yakan_ryoukin = np.round(hiru_ryoukin*1.3,decimals=-1)
    #結果の表示
    print(f"距離{kyori}mのとき、昼間:{hiru_ryoukin:.0f}円 夜間:{yakan_ryoukin:.0f}円")