import matplotlib.pyplot as plt
import numpy as np

x = np.arange(99.1, 99.9, 0.1)
data_cdc_ts = [0.9329, 0.9327, 0.9322, 0.9317, 0.9312, 0.9163, 0.8365, 0.7416, 0.5402]
data_cdc_ce = [0.8718, 0.8458, 0.8018, 0.7235, 0.6568, 0.5498, 0.407, 0.2463, 0.0895]
data_cdc_cp = [0.823, 0.7701, 0.6897, 0.5998, 0.511, 0.4074, 0.2854, 0.1674, 0.0599]

data_cdc_cusum_ts = [0.9324, 0.9322, 0.932, 0.9314, 0.931, 0.8982, 0.8347, 0.7105, 0.4153]
data_cdc_cusum_ce = [0.8518, 0.8264, 0.7808, 0.6996, 0.6108, 0.4856, 0.3385, 0.1685, 0.0562]
data_cdc_cusum_cp = [0.7988, 0.7476, 0.6759, 0.6046, 0.4844, 0.3916, 0.2361, 0.1273, 0.0451]

data_cdc_sst_ts = [0.9329, 0.9327, 0.9325, 0.9318, 0.9316, 0.9162, 0.8354, 0.7087, 0.4156]
data_cdc_sst_ce = [0.8429, 0.8068, 0.7568, 0.6512, 0.5775, 0.4653, 0.3101, 0.1463, 0.0503]
data_cdc_sst_cp = [0.7668, 0.7147, 0.6424, 0.5484, 0.4475, 0.3156, 0.1938, 0.0734, 0.0353]

if __name__ == '__main__':
    # print(np.array(data_bdc_ts)[:, 0])
    f, ax = plt.subplots(figsize=(10, 6))
    # plt.figure(figsize=(10, 8))
    plt.title('')  # 折线图标题
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('MAPA', fontdict={'size': 20})  # x轴标题
    plt.xticks(x, fontsize=15)
    plt.ylabel('Compression Ratio (CR)', fontdict={'size': 20})  # y轴标题
    plt.yticks(np.arange(0, 1.1, 0.1), fontsize=15)
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

    plt.savefig("cdcCR.eps", bbox_inches='tight')
    plt.show()  # 显示折线图
