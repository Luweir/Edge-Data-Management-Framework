import matplotlib.pyplot as plt
import numpy as np

x = np.arange(99.1, 99.9, 0.1)
data_cdc_ts = [0.0602, 0.0647, 0.0706, 0.0787, 0.0869, 0.1087, 0.135, 0.129, 0.2217]
data_cdc_ce = [0.0736, 0.097, 0.1314, 0.1675, 0.1557, 0.1896, 0.2332, 0.2621, 0.2911]
data_cdc_cp = [0.104, 0.1364, 0.1727, 0.2068, 0.204, 0.2356, 0.2617, 0.2795, 0.291]

data_cdc_cusum_ts = [1.1618, 1.2863, 1.4465, 1.6854, 1.8321, 3.1548, 4.5679, 8.2381, 11.8143]
data_cdc_cusum_ce = [1.6228, 2.1642, 2.6875, 3.9542, 4.349, 5.8954, 7.6639, 8.624, 9.9241]
data_cdc_cusum_cp = [1.8515, 2.3564, 2.8531, 3.3274, 4.0416, 4.6851, 5.0873, 6.3125, 7.1607]

data_cdc_sst_ts = [1.5897, 1.6082, 1.6204, 1.8257, 2.0982, 3.8941, 4.936, 8.6948, 11.3294]
data_cdc_sst_ce = [2.5985, 2.8328, 3.1926, 3.8124, 4.4201, 6.1743, 7.9442, 8.0983, 8.247]
data_cdc_sst_cp = [3.3389, 3.6184, 4.0217, 4.5127, 4.8375, 5.678, 6.7509, 7.1127, 7.3465]

if __name__ == '__main__':
    # print(np.array(data_bdc_ts)[:, 0])
    f, ax = plt.subplots(figsize=(10, 6))
    # plt.figure(figsize=(10, 8))
    plt.title('')  # 折线图标题
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('MAPA', fontdict={'size': 20})  # x轴标题
    plt.xticks(x, fontsize=15)
    plt.ylabel('Execution Time (s)', fontdict={'size': 20})  # y轴标题
    plt.yticks(np.arange(0, 14, 2), fontsize=15)
    ax.set_xticklabels(
        ["99.1", "99.2", "99.3", "99.4", "99.5", "99.6", "99.7", "99.8", "99.9"])
    # ax.set_yticklabels(
    #     ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
    marker_size = 6
    plt.plot(x, data_cdc_ts, marker='o', markersize=marker_size)  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(x, data_cdc_ce, marker='^', markersize=marker_size)
    plt.plot(x, data_cdc_cp, marker='s', markersize=marker_size)
    plt.plot(x, data_cdc_cusum_ts, marker='o', markersize=marker_size)
    plt.plot(x, data_cdc_cusum_ce, marker='^', markersize=marker_size)
    plt.plot(x, data_cdc_cusum_cp, marker='s', markersize=marker_size)
    plt.plot(x, data_cdc_sst_ts, marker='o', markersize=marker_size)
    plt.plot(x, data_cdc_sst_ce, marker='^', markersize=marker_size)
    plt.plot(x, data_cdc_sst_cp, marker='s', markersize=marker_size)
    # font_size = 8
    #
    # count = 0
    # for a, b in zip(x, data_bdc_ts):
    #     if count > 14:
    #         plt.text(a, b - 0.03, b, ha='center', va='bottom', fontsize=font_size)  # 设置数据标签位置及大小
    #     else:
    #         count += 1
    # count = 0
    # for a, b in zip(x, data_bdc_ce):
    #     if count > 9:
    #         plt.text(a, b + 0.02, b, ha='center', va='center', fontsize=font_size)
    #     else:
    #         count += 1
    # count = 0
    # for a, b in zip(x, data_bdc_cp):
    #     if count > 7:
    #         plt.text(a - 0.2, b - 0.03, b, ha='center', va='center', fontsize=font_size)
    #     else:
    #         count += 1
    # for a, b in zip(x, data_cdc_ts):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=font_size)
    # count = 0
    # for a, b in zip(x, data_cdc_ce):
    #     if count > 8:
    #         plt.text(a + 0.3, b + 0.02, b, ha='center', va='center', fontsize=font_size)
    #     else:
    #         count += 1
    # count = 0
    # for a, b in zip(x, data_cdc_cp):
    #     if count > 8:
    #         plt.text(a - 0.1, b - 0.02, b, ha='center', va='center', fontsize=font_size)
    #     else:
    #         count += 1

    # plt.legend(
    #     ['CDC TS', 'CDC CE', 'CDC CP', 'CDC-CUSUM TS', 'CDC-CUSUM CE', 'CDC-CUSUM CP', 'CDC-SST TS', 'CDC-SST CE',
    #      'CDC-SST CP'],
    #     bbox_to_anchor=(1.05, 1), ncol=1, borderaxespad=0, prop={'size': 15})
    plt.legend(
        ['CDC TS', 'CDC CE', 'CDC CP', 'CDC-CUSUM TS', 'CDC-CUSUM CE', 'CDC-CUSUM CP', 'CDC-SST TS', 'CDC-SST CE',
         'CDC-SST CP'], prop={'size': 14})

    plt.savefig("cdcExecutionTime.eps", bbox_inches='tight')
    plt.show()  # 显示折线图
