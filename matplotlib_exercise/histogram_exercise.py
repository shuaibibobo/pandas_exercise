import pandas as pd
import os
from matplotlib import pyplot as plt
# 折线图主要是看内容随时间变化的趋势情况

plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


print(os.getcwd())
df=pd.read_excel(r'.\data\house_data.xlsx')
# cumulative累积分布直方图
df['均价'].plot(kind='hist',color='violet',legend=True,
              edgecolor='b',title='上海徐州二手房均价分布图',
              cumulative=True)
plt.xlabel('均价（元）')
plt.ylabel('计数')
plt.show()