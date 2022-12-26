import matplotlib.pyplot as plt
import numpy as np

# data_bdc_ts = [[0.9327, 0.0587], [0.9325, 0.0628], [0.9323, 0.0695], [0.9318, 0.0764], [0.9311, 0.0862],
#                [0.9154, 0.1083], [0.8348, 0.1518], [0.6917, 0.2291], [0.4153, 0.3541]]
# data_bdc_ce = [[0.8364, 0.1393], [0.7859, 0.1718], [0.7254, 0.2145], [0.6458, 0.2569], [0.5508, 0.3053],
#                [0.4351, 0.3475], [0.3045, 0.3961], [0.1165, 0.4412], [0.0457, 0.4717]]
# data_bdc_cp = [[0.7498, 0.2002], [0.6770, 0.2378], [0.5929, 0.2776], [0.5033, 0.3170], [0.4070, 0.3541],
#                [0.3040, 0.3964], [0.1839, 0.4319], [0.0928, 0.4542], [0.0272, 0.4669]]

data_cdc_ts = [[0.9329, 0.0602], [0.9327, 0.0647], [0.9322, 0.0706], [0.9317, 0.0787], [0.9312, 0.0869],
               [0.9163, 0.1087], [0.8365, 0.1350], [0.7416, 0.1290], [0.5402, 0.2217]]
data_cdc_ce = [[0.8718, 0.0736], [0.8458, 0.0970], [0.8018, 0.1314], [0.7235, 0.1675], [0.6568, 0.1557],
               [0.5498, 0.1896], [0.4070, 0.2332], [0.2463, 0.2621], [0.0895, 0.2911]]
data_cdc_cp = [[0.8230, 0.1040], [0.7700, 0.1364], [0.6897, 0.1727], [0.5998, 0.2068], [0.5110, 0.2040],
               [0.4074, 0.2356], [0.2854, 0.2617], [0.1674, 0.2795], [0.0599, 0.2910]]
if __name__ == '__main__':
    # print(np.array(data_bdc_ts)[:, 0])
    plt.figure(figsize=(10, 6))
    plt.title('')  # 折线图标题
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('Compression Ratio (CR)', fontdict={'size': 20})  # x轴标题
    plt.xticks(fontsize=15)
    plt.ylabel('Average Execution Time (s)', fontdict={'size': 20})  # y轴标题
    plt.yticks(fontsize=15)
    # plt.plot(np.array(data_bdc_ts)[:, 0], np.array(data_bdc_ts)[:, 1], marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
    # plt.plot(np.array(data_bdc_ce)[:, 0], np.array(data_bdc_ce)[:, 1], marker='o', markersize=3)
    # plt.plot(np.array(data_bdc_cp)[:, 0], np.array(data_bdc_cp)[:, 1], marker='o', markersize=3)
    plt.plot(np.array(data_cdc_ts)[:, 0], np.array(data_cdc_ts)[:, 1], marker='o', markersize=8)
    plt.plot(np.array(data_cdc_ce)[:, 0], np.array(data_cdc_ce)[:, 1], marker='^', markersize=8)
    plt.plot(np.array(data_cdc_cp)[:, 0], np.array(data_cdc_cp)[:, 1], marker='s', markersize=8)

    # for a, b in zip(x, y1):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
    # for a, b in zip(x, y2):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    # for a, b in zip(x, y3):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    # for a, b in zip(x, y4):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    # for a, b in zip(x, y5):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.legend(['CDC-TS', 'CDC-CE', 'CDC-CP'], prop={'size': 15})  # 设置折线名称
    plt.savefig("crTime.eps", bbox_inches='tight')
    plt.show()  # 显示折线图
