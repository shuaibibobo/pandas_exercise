import pandas as pd
import os
from matplotlib import pyplot as plt
# 折线图主要是看内容随时间变化的趋势情况

plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


print(os.getcwd())
df=pd.read_excel(r'.\data\user_analysis.xlsx')
# 去掉空值行
df.dropna(axis=0)
# 设置图框的大小
fig=plt.figure(figsize=(8,4))
plt.plot(df['时间'],df['新关注人数'],
         color='m',
         label='新关注人数')
plt.plot(df['时间'],df['取消关注人数'],
         marker='o',
         markersize=5,
         color='r',
         markerfacecolor='orangered',
         label='取消关注人数')
plt.plot(df["时间"],df['净增关注人数'],
         color='g',
         label='净增关注人数')

plt.title('公众号每天新增用户数')
plt.xlabel('日期')
plt.ylabel('新增人数')
# X轴文字旋转45°
fig.autofmt_xdate(rotation=45)
plt.legend()
plt.show()