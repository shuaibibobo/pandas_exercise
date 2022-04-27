import pandas as pd
from matplotlib import pyplot as plt

f=open('data/iris.csv')
iris=pd.read_csv(f)
colors=['#9999ff','#ff9999','#1245ff']
Species=iris.Species.unique()
# for i in range(len(Species)):
#     plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'],
#                 iris.loc[iris.Species == Species[i], 'Petal.Width'],
#                 s = 35, c = colors[i], label = Species[i])
#


for i in range(len(Species)):

    plt.scatter(iris.loc[iris.Species==Species[i],'Petal.Length'],
                iris.loc[iris.Species==Species[i],'Petal.Width'],
                s=35,c=colors[i],label=Species[i])
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title("花瓣长度与宽度的关系")
plt.xlabel("花瓣长度")
plt.ylabel("花瓣宽度")
plt.legend(loc='upper left')
plt.show()

# 结论 长度宽度存在正向关系