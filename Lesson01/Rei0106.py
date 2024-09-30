"""
実行例　while文
"""

print("1+2+3+...が50を超えるまで計算する")
s = 0
i = 1
while s<50:
    s += i
    print(f"i={i}  s={s}")
    i += 1  #Pythonで i++ は使えません
