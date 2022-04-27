import pandas as pd
import numpy as np

f=open('15house-data.csv',encoding='utf-8')
df=pd.read_csv(f)
# print(df.head(3))
# s=df[df['物业费']=='暂无资料']
# print(s)
df.loc[df['物业费']=='暂无资料','物业费']=np.NAN
# print(df.head(3))
# 表信息
# print(df.info())
# 字段信息
# print(df.columns)
# 表字段类型
# print(df.dtypes)
# 缺失值
# print(df.isnull())
# 字段缺失值
# print(df.isnull().any())
# 缺失值统计
# print(df.isnull().sum()/df.count())
# 删除缺失值 针对列
# df.drop('参考月供',axis=1)
# 获取描述性统计信息
# print(df.describe())

df.to_csv('house_data.csv',index_label=False)