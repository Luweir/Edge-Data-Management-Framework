import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# plt.figure(figsize=(13, 4))
# 构造x轴刻度标签、数据
labels = ['TS', 'CE', 'CP']

sub1_odc = [0.7, 0.15, 0.146]
sub1_fdr = [0.76, 0.06, 0.05]
sub1_bdc = [0.79, 0.31, 0.22]
sub1_cdc = [0.8, 0.49, 0.3]

sub2_odc = [0.72, 0.25, 0.205]
sub2_fdr = [0.92, 0.08, 0.05]
sub2_bdc = [0.928, 0.47, 0.405]
sub2_cdc = [0.93, 0.69, 0.61]

sub3_odc = [0.745, 0.85, 0.62]
sub3_fdr = [0.93, 0.9, 0.43]
sub3_bdc = [0.925, 0.92, 0.79]
sub3_cdc = [0.925, 0.92, 0.82]

figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4), dpi=300, )
# 两组数据
# plt.subplot(131)
x = np.arange(len(labels))  # x轴刻度标签位置

lable_size = 15
ticks_size = 12

width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5 * width, sub1_odc, width, label='ODC')
ax1.bar(x - 0.5 * width, sub1_fdr, width, label='FDR')
ax1.bar(x + 0.5 * width, sub1_bdc, width, label='BDC')
ax1.bar(x + 1.5 * width, sub1_cdc, width, label='CDC')

# ax1.ylabel('Execute time')
ax1.set_title('SubDataset1', size=lable_size)
# x轴刻度标签位置不进行计算
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.tick_params(labelsize=ticks_size)
ax1.set_ylabel('Compression Ratio (CR)', size=lable_size)
ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], size=ticks_size)
ax1.legend(ncol=1)


# plt.subplot(132)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width，x， x + width即每组数据在x轴上的位置
ax2.bar(x - 1.5 * width, sub2_odc, width, label='ODC')
ax2.bar(x - 0.5 * width, sub2_fdr, width, label='FDR')
ax2.bar(x + 0.5 * width, sub2_bdc, width, label='BDC')
ax2.bar(x + 1.5 * width, sub2_cdc, width, label='CDC')
ax2.set_title('SubDataset2', size=lable_size)
# x轴刻度标签位置不进行计算
ax2.set_xticks(x)
ax2.tick_params(labelsize=ticks_size)
ax2.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax2.set_xticklabels(labels)


# plt.subplot(133)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax3.bar(x - 1.5 * width, sub3_odc, width, label='ODC')
ax3.bar(x - 0.5 * width, sub3_fdr, width, label='FDR')
ax3.bar(x + 0.5 * width, sub3_bdc, width, label='BDC')
ax3.bar(x + 1.5 * width, sub3_cdc, width, label='CDC')
ax3.set_title('SubDataset3', size=lable_size)
# x轴刻度标签位置不进行计算
ax3.set_xticks(x)
ax3.tick_params(labelsize=ticks_size)
ax3.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax3.set_xticklabels(labels)

plt.savefig("compression_ratio.eps", bbox_inches='tight')
plt.show()
