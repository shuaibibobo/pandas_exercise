from matplotlib import pyplot as plt
import numpy as np

data=np.arange(10)
print(data)
# plt.plot(data,lw=5,color='r',linestyle=':',marker='o')
plt.plot(data,color='r')
plt.legend('y')
plt.title('简单可视化')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('x')
plt.ylabel('y')
plt.style.use('ggplot')
plt.annotate('标注文字',xy=(2.5,4))
plt.annotate('标注文字2',xy=(6,6),xytext=(4,8),arrowprops=dict(facecolor='black'))
plt.show()