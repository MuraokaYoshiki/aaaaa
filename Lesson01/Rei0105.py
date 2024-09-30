"""
range関数の実行例
"""

print( f"第1引数のみ{list(range(5))}" )     #0,1,2,3,4 (0から5未満まで)
print( f"第１と2引数{list(range(3,6))}" )   #3,4,5(3から6未満)
print( f"第１,2,3引数{list(range(0,10,2))}" ) #0,2,4,..,8(0から10未満 増分２)
print( f"第3引数が負数の場合{list(range( 10, 2, -2))}" ) #10から2未満，増分-2

""""
print("=========ex1========")
s = 0
for i in range(5):
    s += i
    print( f"i={ i }  s={s } " )

print("=========ex2========")
s = 0
for i in range(3,7):
    s += i
    print( f"i= {i}  s={s}")

print("=========ex3========")
s = 0
for i in range(0,10,2):
    s += i
    print( f"i={i}  s={s}" )

print("=========s4=========)
s = 0
for i in [20,15,25,30,50]:
    s += i
    print( f"i={i}  s={s}" )
"""
