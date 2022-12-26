import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

x = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2205]

yr = [0, 0.175, 0.283, 0.341, 0.326, 0.355, 0.342, 0.376, 0.416, 0.449, 0.46]
yr1 = [1, 0.832, 0.723, 0.664, 0.678, 0.648, 0.66, 0.626, 0.586, 0.553, 0.541]
yr11 = [1, 0.825, 0.717, 0.659, 0.674, 0.645, 0.658, 0.624, 0.584, 0.551, 0.54]

ticks_size = 15
width = 50  # 柱子的宽度
lable_size = 20
legend_size = 15
text_size = 12
x = np.array(x)
plt.bar(x - width, yr, width=width, label='R')
plt.bar(x, yr1, width=width, label='R1')
plt.bar(x + width, yr11, width=width, label='R1\'')
plt.xticks(x, size=ticks_size)
plt.yticks(size=ticks_size)
plt.legend(prop={'size': legend_size})
plt.ylabel(u'Ratio', size=lable_size)  # 设置x轴名称
plt.xlabel(u'Number of segments', size=lable_size)  # 设置y轴名称
for a, b in zip(x, yr):
    plt.text(a - width, b, b, ha='center', va='bottom', fontsize=text_size)
for a, b in zip(x, yr1):
    plt.text(a, b - 0.05, b, ha='center', va='bottom', fontsize=text_size)
for a, b in zip(x, yr11):
    plt.text(a + width, b, b, ha='center', va='bottom', fontsize=text_size)
plt.savefig('different_seg_quantities.eps', bbox_inches='tight')
plt.show()
