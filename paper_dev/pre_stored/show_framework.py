import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# QLMS = [0.5213,	0.6611,	0.8082,	0.8684,	0.8905,	0.9286,	0.9286,	0.9286,	0.9286]
# HLMS = [0.7317,	0.7436,	0.8669,	0.9165,	0.9133,	0.9112,	0.9112,	0.9112,	0.9112]
# AMI = [0.7113,	0.7445,	0.8687, 0.9286,	0.9286,	0.9286,	0.9286,	0.9286,	0.9286]
# framework = [0.7517,	0.8605,	0.9117,	0.9548,	0.9628,	0.9632,	0.9636,	0.9639,	0.9639]

QLMS = [0.5213, 0.6611, 0.8082, 0.8684, 0.8905, 0.9286, 0.9486, 0.9586, 0.9586]
x1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

HLMS = [0.7317, 0.7445, 0.7536, 0.7612, 0.7856, 0.8056, 0.8569, 0.8819, 0.9165, 0.9233, 0.9378, 0.9412, 0.9412, 0.9412]
x2 = [0.1, 0.15, 0.2, 0.225, 0.25, 0.275, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

AMI = [0.7113, 0.7312, 0.7545, 0.7896, 0.7896, 0.8112, 0.8587, 0.8945, 0.9286, 0.9486, 0.9486, 0.9586, 0.9586, 0.9586]
x3 = [0.1, 0.15, 0.2, 0.225, 0.25, 0.275, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

framework = [0.7517, 0.8605, 0.9117, 0.9548, 0.9628, 0.9632, 0.9636, 0.9639, 0.9639]
x4 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

x_new = np.arange(0.1, 0.9, 0.05)

# func = interpolate.interp1d(x, QLMS, kind='cubic')
# y_smooth = func(x_new)
# plt.plot(x_new, y_smooth)

plt.xlabel('MAPE', size=20)  # 设置x轴名称
plt.ylabel(u'缩减率', size=20)  # 设置y轴名称
# plt.xlim((0, 1))  # 设置x轴范围
# plt.ylim((0, 1))  # 设置y轴范围
plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], size=20)  # 设置x轴刻度
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], size=18)  # 设置y轴刻度

func1 = interpolate.interp1d(x1, QLMS, kind='cubic')
y_smooth = func1(x_new)
plt.plot(x_new, y_smooth, label="QLMS", marker='o')

func2 = interpolate.interp1d(x2, HLMS, kind='cubic')
y_smooth = func2(x_new)
plt.plot(x_new, y_smooth, label="HLMS", marker='s')

func3 = interpolate.interp1d(x3, AMI, kind='cubic')
y_smooth = func3(x_new)
plt.plot(x_new, y_smooth, label="AMI", marker='*')

func4 = interpolate.interp1d(x4, framework, kind='cubic')
y_smooth = func4(x_new)
plt.plot(x_new, y_smooth, label="Our Architecture", marker='^')

# plt.plot(x1, QLMS, label="QLMS")
# plt.plot(x2, HLMS, label="HLMS")
# plt.plot(x3, AMI, label="AMI")
# plt.plot(x4, framework, label="Our framework")

plt.legend(loc="lower right", prop={'size': 18})  # 添加注解
plt.grid(linestyle='-.')  # 生成网格
plt.show()
