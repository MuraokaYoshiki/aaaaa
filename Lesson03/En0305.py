#演習５
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

#最低時給と人口密度
prefecture=['北海道','青 森','岩 手','宮 城','秋 田','山 形','福 島',
    '茨 城','栃 木','群 馬','埼 玉','千 葉','東 京','神奈川','新 潟','富 山',
    '石 川','福 井','山 梨','長 野','岐 阜','静 岡','愛 知','三 重','滋 賀',
    '京 都','大 阪','兵 庫','奈 良','和歌山','鳥 取','島 根','岡 山','広 島',
    '山 口','徳 島','香 川','愛 媛','高 知','福 岡','佐 賀','長 崎','熊 本',
    '大 分','宮 崎','鹿児島','沖 縄'
]
h_wage=np.array([
    889,822,821,853,822,822,828,879,882,865,956,953,1041,1040,
    859,877,861,858,866,877,880,913,955,902,896,937,992,928,866,859,
    821,824,862,899,857,824,848,821,820,870,821,821,821,822,821,821,820
])
p_density=np.array([
    68.6,135.6,83.8,320.5,87.9,120.5,138.9,478.4,308.1,310.1,1913.4,1206.5,
    6168.7,3777.7,183.1,251,275.7,187.7,187,154.8,191.3,475.8,1446.7,314.5,
    351.7,566,4639.8,658.8,369.6,203.9,163.5,103.5,270.1,335.4,229.8,182.3,
    520.2,244.1,102.5,1023.1,341.2,333.3,241.1,183.9,142.7,179.4,628.4
])

#相関係数の計算


#回帰直線の計算


#回帰直線のための座標計算


#散布図

#回帰直線

plt.title("最低時給－人口密度の散布図")
plt.xlabel("最低時給")
plt.ylabel("人口密度")
plt.legend()
plt.savefig("./img/En0205.png")