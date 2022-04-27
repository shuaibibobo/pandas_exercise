import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
f=open('data/cars.csv')
cars=pd.read_csv(f)
# x轴数据为汽车速度 Y轴数据为刹车距离 S为点大小 C为点颜色
# MARKER为点的形状 ALPHA为点透明度 linewidths为点边界粗细 edgecolors为散点边界颜色
plt.scatter(cars.speed,cars.dist,s=30,c='steelblue',marker='s',alpha=0.9,linewidths=0.3,edgecolors='red')
plt.title('汽车速度和刹车距离的关系')
plt.xlabel('汽车速度')

plt.ylabel('刹车距离')
# 去除图边框的顶部刻度和右边刻度
# plt.tick_params(top='on',right='on')
plt.show()

# 散点图主要用于二维数据可视化 探求不同变量之间的关系
# 结论：汽车刹车速度与刹车距离存在正相关关系 随着速度增加刹车距离增加