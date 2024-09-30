#例題４　棒グラフ
import matplotlib.pyplot as plt
import japanize_matplotlib

#関東地方の都道府県名と最低賃金のデータ
prefecture = ["茨城","栃木","群馬","埼玉","千葉","東京","神奈川"]
h_wage = [879,882,865,956,953,1041,1040]

#棒グラフの設定
#【入力】

plt.title("時給")
plt.xlabel("都道府県名")
plt.ylabel("円")
#plt.show()
plt.savefig("./img/Rei0304.png")
plt.close()
