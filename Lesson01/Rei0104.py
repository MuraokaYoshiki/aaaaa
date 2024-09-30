"""
例題４
if文の例題　　蛇足ですが，ダブルコーテーション3つで複数行のコメントになります
"""
import random
siken = random.randint(0,100)
#行末の:はブロックの始まり　ブロックはインデントをつける
if siken >= 80:
    hyouka = "素晴らしい"
#ブロックの終わりは、インデントを戻す
elif siken >= 60:
    hyouka = "合格"
else:
    hyouka = "不合格"

print( "試験結果"  , siken , hyouka)