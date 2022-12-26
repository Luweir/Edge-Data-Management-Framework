import matplotlib.pyplot as plt
import numpy as np

x = np.arange(19)
# data_bdc_ts = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.9327, 0.9325, 0.9323, 0.9318,
#                0.9311, 0.9154, 0.8348, 0.6917, 0.4153]
# data_bdc_ce = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.8738, 0.8364, 0.7859, 0.7254, 0.6458,
#                0.5608, 0.4851, 0.3045, 0.1465, 0.0457]
# data_bdc_cp = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.928, 0.807, 0.7498, 0.677, 0.5929, 0.5033,
#                0.407, 0.304, 0.1839, 0.0928, 0.0272]

data_cdc_ts = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.9327, 0.9325, 0.9323, 0.9318,
               0.9311, 0.9163, 0.8365, 0.7416, 0.5402]
data_cdc_ce = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.9022, 0.8718, 0.8458, 0.8018, 0.7235,
               0.6568, 0.5498, 0.407, 0.2463, 0.0895]
data_cdc_cp = [0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.933, 0.8738, 0.823, 0.77, 0.6897, 0.5998,
               0.511, 0.4074, 0.2854, 0.1674, 0.0599]
if __name__ == '__main__':

    # print(np.array(data_bdc_ts)[:, 0])
    f, ax = plt.subplots(figsize=(10, 6))
    # plt.figure(figsize=(10, 8))
    plt.title('')  # 折线图标题
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('MAPA', fontdict={'size': 20})  # x轴标题
    plt.xticks(x, fontsize=12)
    plt.ylabel('Compression Ratio (CR)', fontdict={'size': 20})  # y轴标题
    plt.yticks(np.arange(0, 1.1, 0.1), fontsize=13)
    ax.set_xticklabels(
        ["90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "99.1", "99.2", "99.3", "99.4", "99.5", "99.6",
         "99.7", "99.8", "99.9"])
    # ax.set_yticklabels(
    #     ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
    marker_size = 6
    # plt.plot(x, data_bdc_ts, marker='o', markersize=marker_size)  # 绘制折线图，添加数据点，设置点的大小
    # plt.plot(x, data_bdc_ce, marker='^', markersize=marker_size)
    # plt.plot(x, data_bdc_cp, marker='s', markersize=marker_size)
    plt.plot(x, data_cdc_ts, marker='o', markersize=marker_size)
    plt.plot(x, data_cdc_ce, marker='^', markersize=marker_size)
    plt.plot(x, data_cdc_cp, marker='s', markersize=marker_size)


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

    # plt.legend(['BDC-TS', 'BDC-CE', 'BDC-CP', 'CDC-TS', 'CDC-CE', 'CDC-CP'], prop={'size': 15})  # 设置折线名称
    plt.legend(['CDC-TS', 'CDC-CE', 'CDC-CP'], prop={'size': 15})  # 设置折线名称
    plt.savefig("overall_cr_mapa_10.eps", bbox_inches='tight')
    plt.show()  # 显示折线图
