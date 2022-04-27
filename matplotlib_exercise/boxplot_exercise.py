import pandas as pd
from matplotlib import pyplot as plt

f=open('data/titanic_train.csv')
titanic=pd.read_csv(f)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
titanic.dropna(subset=['Age'],inplace=True)
plt.style.use('ggplot')
#
# plt.boxplot(x=titanic.Age,patch_artist=True, #要求自定义填充盒形图
#             showmeans=True, #以点的形式填充均值
#             boxprops={'color':'black','facecolor':'#9999ff'},#设置箱体属性
#             flierprops={'marker':'o','markerfacecolor':'red','color':'black'},#设置异常值属性
#             meanprops={'marker':'D','markerfacecolor':'indianred'},#设置均值点属性
#             medianprops={'linestyle':'-','color':'orange'})#设置中位线属性
# # 设置Y轴范围
# plt.ylim(0,85)
# plt.tick_params(top='off',right='off')
# plt.show()

# 结论：乘客平均年龄在30岁，有四分之一超过38.四分之一低于20岁

titanic.sort_values(by='Pclass',inplace=True)
Age=[]
levels=titanic.Pclass.unique()
for Pclass in levels:
    Age.append(titanic.loc[titanic.Pclass==Pclass,'Age'])

plt.boxplot(x=Age,patch_artist=True,
            labels=['一等舱','二等舱','三等舱'],
            showmeans=True,
            boxprops={'color':'black','facecolor':'#9999ff'},#设置箱体属性
            flierprops={'marker':'o','markerfacecolor':'red','color':'black'},#设置异常值属性
            meanprops={'marker':'D','markerfacecolor':'indianred'},#设置均值点属性
            medianprops={'linestyle':'-','color':'orange'})#设置中位线属性)
plt.show()

# 箱线图用于展现数据分布（上下四分位值、中位数等），也可以反映数据的异常情况
# 如果对人群的年龄按不同的舱位来看，我们会发现一个明显的趋势，就是舱位等级越高的乘客，他们的年龄越高，三种舱位的平均年龄为38、30和25，
# 说明年龄越是偏大一点，他们的经济能力会越强一些，所买的舱位等级可能就会越高一些。同时，在二等舱和三等舱内，乘客的年龄上存在一些异常用户