############# Tukey_Cramer の多重分析モジュール ########
def tukey_hsd( ind, *args ):
    import pandas as pd
    import numpy as np
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    data_arr = np.hstack( args ) 
    ind_arr = np.array([])
    for x in range(len(args)):
        ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x]))) 
    print(pairwise_tukeyhsd(data_arr,ind_arr))

import pandas as pd
from mydblib2 import my_select

print("【T122142】 小問番号0")

#tableに検索するtable 名
sqlstring = f"""
    SELECT Croom, Math, Eng, Jpn 
    FROM siken
    ;
"""
#wptest データベースの siken テーブルのレコードを読み込み
siken = my_select("wptest", sqlstring)

#classが A と B と C を抽出 Math 列のみ
class_A = siken.query("Croom == 'A'")["Math"]
class_B = siken.query("Croom == 'B'")["Math"]
class_C = siken.query("Croom == 'C'")["Math"]

#クラブ活動別に平均値の表示
ans = siken.groupby("Croom").mean()
print(ans)

mean_math = siken.groupby("Croom")["Math"].mean()

from scipy.stats import f_oneway

f_val,p_val = f_oneway(class_A, class_B, class_C)

print( f"Engについて 一元配置分散分析 f_value={f_val:.3f} p_value={p_val:.3f}")
tukey_hsd(["A", "B", "C"], class_A, class_B, class_C)