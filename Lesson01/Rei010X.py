#例題７
#array1はリストであることを宣言
array1 = [] #array1はリストであることを宣言
#array1 = list()
array1.append( 0 )  #リストに値の追加
array1.append( 10 )
array1.append( 20 ) 
print( "array1=" , array1 )
array1[1] = 100
print( "array1=" , array1 )

#宣言と初期化
array2 = [0 , 1]
array3 = [0 , 1, 1, 2, 3, 5, 8]
array4 = list(range( 0, 50 ,10))  #range(start,end,step)
print( "array2=" , array2 )
print( "array3=" , array3 )
print( "array4=" , array4 )

#for文で利用可能
sosuu = [2,3,5,7,11,13]
for i in sosuu:
    print( f"i={i} ",end="*** ")
print("\n")
#要素数の参照
print( "List sosuuの要素数は",len(sosuu))

#条件のあったリストを作成
mul3_num = [ num*3 for num in range(10) ] #３の倍数10個のリスト
even_num2 = [ num*num for num in range(10)  if num % 2 == 0 ] #numが0,1,2,3,で ，num%2==0が成り立つときだけ，
print("mul3_num=" , mul3_num)
print("even_num2=" , even_num2)

