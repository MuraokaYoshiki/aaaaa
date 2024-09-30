import pandas as pd
from mydblib import my_select
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

sqlstring = """
        SELECT answer1,COUNT(answer1) AS pcnt
        FROM quest
        GROUP BY answer1
        ;
"""
recset = my_select(sqlstring)

recset["answer1"] = recset["answer1"].astype(int)

print(f"検索結果\n{recset}")
plt.bar(recset["answer1"], recset["pcnt"], align="center", tick_label=recset["answer1"])
plt.title("アンケートテーブル集計結果")
plt.xlabel("アンケート回答")
plt.ylabel("人数")
plt.savefig("./img/En0309.png")
plt.close()
