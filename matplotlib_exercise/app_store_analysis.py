import pandas as pd
import os
from matplotlib import pyplot as plt
import  seaborn as sns
# 折线图主要是看内容随时间变化的趋势情况

# plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

app=pd.read_csv(r'.\data\w1_applestore.csv')
app['size_mb']=app['size_bytes']/(1024*1024.0)
app['size_mb']=app['size_mb'].round(0)
app['paid']=app['price'].apply(lambda x:1 if x>0 else 0)
app.paid.describe()
# print(app.paid.describe())
# 清洗异常值（unamed） 给分析造成难度的值（size_bytes） 核心变量的创建（免费/收费）
# 2.数据的分组分析及可视化
#每一种价格对应的app数量
# print(app.price.value_counts())
# 删除价格大于等于49.99的app
app=app[app['price']<=49.99]
bins=[0,2,10,300]
labels=['<2','<10','<300']
app['price_new']=pd.cut(app.price,bins,right=False,labels=labels)
# print(app.groupby(['price_new'])['price'].describe())
# 不同类型app的价格分布
# print(app.groupby(['prime_genre'])['price'].describe())
#  用户评价数据分布
app.rating_count_tot.describe()
# 对用户打分进行分组
bins=[0,1000,5000,1000000,5000000]
app['rating_news']=pd.cut(app.rating_count_tot,bins,right=False)
# 用户打分与价格之间的关系
# print(app.groupby(['rating_news'])['price'].describe())

# sns.relplot(x='prime_genre',y='user_rating',kind='line',data=app)  #折线图
# plt.xticks(rotation="90")
# app1=app[app['price']<=9.99]
# # 直方图，APP价格方向
# sns.displot(app1['price'])

# 业务问题1：收费App的价格分布是如何的？不同类别之间有关系吗？
app2=app[app['price']<=30]
plt.figure(figsize=(20,16))
sns.boxplot(x='price',y='prime_genre',data=app2[app2['paid']==1])
plt.show()
# 业务解答：价格大部分集中在9.9美元以内，个别类别（如医疗）等因专业性总体价格会高于其他类别

# print(app.groupby(['prime_genre'])[['id']].count().sort_values('id',ascending=False))
# 只保留前五个类别数据
app2=app[app['price']<=30]
top5=['Games','Entertainment','Education','Photo & Video','Utilities']
app5=app2[app2.prime_genre.isin(top5)]
plt.figure(figsize=(10,8))
data=app5[app5['paid']==1]
sns.boxplot(x='price',y='prime_genre',data=data)
# plt.show()

# 散点图：价格和用户评价的分布
app3=app[app['price']<=50]
sns.scatterplot(x='price',y='user_rating',data=app3)
# plt.show()

# 只保留5个数据类别
app2=app[app['price']<=30]
top5=['Games','Entertainment','Education','Photo & Video','Utilities']
app5=app2[app2.prime_genre.isin(top5)]
plt.figure(figsize=(10,8))
sns.barplot(x='prime_genre',y='user_rating',hue='paid',data=app5)
# plt.show()

# 业务问题2：免费和收费的App集中在哪些
#第一步：将数据加总成每个类别有多少个app
#第二部：从高到底进行排列
#第三部：将数据进行可视化

plt.figure(figsize=(20,10))
sns.countplot(y='prime_genre',hue='paid',data=app,order=app['prime_genre'].value_counts().index)
plt.tick_params(labelsize=20)
# plt.show()
# 结论：免费和收费APP主要集中在Games

# 业务问题3：免费与收费的App在不同的评分区间的分布
bins=[0,0.1,2.5,4.5,5]
app['rating_lever']=pd.cut(app.user_rating,bins,right=False)
app.groupby(['rating_lever'])['user_rating'].describe()
plt.figure(figsize=(10,8))
sns.countplot(x='paid',hue='rating_lever',data=app)
# plt.show()
# 结论：主要集中在2.5-5之间

# 业务问题4：App的大小和用户评分之间有关系吗？
q4=['user_rating','price','size_mb']
print(app[q4].corr())
plt.figure(figsize=(5,4))
sns.heatmap(app[q4].corr(),annot=True)
plt.show()
# 大小价格都不和评分没有直接关系，但是价格和大小之间有正相关关系