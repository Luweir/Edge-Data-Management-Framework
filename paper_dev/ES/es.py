import ES.esmoothing as esmoothing
import time
import numpy as np
import math


# 以下标k开始分割
def split_data(data, k):
    s_pre = data[:k]
    s_tail = data[k:]
    return s_pre, s_tail


# 缩减算法的核心 时间复杂度O(n^2)
def dataReduce(data, threshold):
    result = []  # 保存每次alpha下的rate值
    alpha = 0.01  # alpha从0.01开始，按步长0.01开始变化增长
    while alpha < 1:
        split_point = 0  # 默认分割点为
        for split_point in range(4, len(data)):  # 切割数据段
            # 划分为两个子数据段train,real。train用于做参数训练，real是预测的值的对比值（真实的数据子集）
            train, real = split_data(data, split_point)
            next_n = len(real)  # 需要向后预测的数据的个数
            predict_n = []  # 存放预测的数据子段
            double_a, double_b = esmoothing.compute_double(alpha, train)  # 计算数据序列的a,b参数
            for nextT in range(1, next_n + 1):
                prediction = double_a[-1] + double_b[-1] * nextT
                predict_n.append(prediction)

            sum = 0.0  # 计算mape值
            for i in range(len(real)):
                sum = sum + abs((real[i] - predict_n[i]) / real[i])
            mape = sum * 100 / len(real)
            if mape < threshold:
                rate = 1 - split_point / len(data)
                result.append(rate)
                break
            else:
                continue
        if split_point == len(data) - 1:
            result.append(0.0)
        alpha = alpha + 0.01
    opt_rate = max(result)
    return opt_rate


# 根据离散度=0.01分割后的数据缩减算法
# def dataSplitReduce(insurance, threshold):
#     # 计算离散系数d=std/mean
#     men = np.mean(insurance)
#     sd = np.std(insurance)
#     d = sd / men
#     # 判断离散系数是否大于0.01,若大于，则表示需要分割，则求最佳分割点
#     if d > 0.01:
#         # 根据T检验求最佳分割点
#         T = []
#         num = len(insurance)
#         for split in range(1, num - 1):
#             x1 = insurance[:split]
#             x2 = insurance[split:]
#             n1 = len(x1)
#             n2 = len(x2)
#             mean_x1 = np.mean(x1)
#             mean_x2 = np.mean(x2)
#             std_x1 = np.std(x1)
#             std_x2 = np.std(x2)
#             sd = (math.sqrt((1.0 / n1) + (1.0 / n2))) * math.sqrt(
#                 ((n1 - 1.0) * (std_x1 ** 2) + (n2 - 1.0) * (std_x2 ** 2)) / (n1 + n2 - 2.0))
#             tep = math.fabs((mean_x1 - mean_x2) / sd)
#             k = split - 1
#             T.append([k, tep])
#
#         Tmax = T[0][1]
#         pos = 1
#         for i in range(1, len(T)):
#             if T[i][1] > Tmax:
#                 Tmax = T[i][1]
#                 pos = i + 1
#
#         # 分割数据为两个子数据段
#         subData1 = insurance[:pos]
#         subData2 = insurance[pos:]
#         # 两个子段分别进行缩减处理
#         if len(subData1) < 5:
#             optRate1 = 0.0
#         else:
#             optRate1 = dataReduce(subData1, threshold)
#         if len(subData2) < 5:
#             optRate2 = 0.0
#         else:
#             optRate2 = dataReduce(subData2, threshold)
#         # 计算总数据段的缩减率
#         Rate = (optRate1 * len(subData1) + optRate2 * len(subData2)) / len(insurance)
#     else:
#         Rate = dataReduce(insurance, threshold)
#     return Rate


# 根据T检验得到的分割点分割数据段，计算数据段的缩减率
def DataReduceByTtest(data):
    # 根据T检验求最佳分割点
    T = []
    num = len(data)
    for split in range(1, num - 1):
        x1 = data[:split]
        x2 = data[split:]
        n1 = len(x1)
        n2 = len(x2)
        mean_x1 = np.mean(x1)
        mean_x2 = np.mean(x2)
        std_x1 = np.std(x1)
        std_x2 = np.std(x2)
        sd = (math.sqrt((1.0 / n1) + (1.0 / n2))) * math.sqrt(
            ((n1 - 1.0) * (std_x1 ** 2) + (n2 - 1.0) * (std_x2 ** 2)) / (n1 + n2 - 2.0))
        tep = math.fabs((mean_x1 - mean_x2) / sd)
        k = split - 1
        T.append([k, tep])

    Tmax = T[0][1]
    pos = 1
    for i in range(1, len(T)):
        if T[i][1] > Tmax:
            Tmax = T[i][1]
            pos = i + 1

    # 分割数据为两个子数据段
    subData1 = data[:pos]
    subData2 = data[pos:]
    # 两个子段分别进行缩减处理
    if len(subData1) < 5:
        optRate1 = 0.0
    else:
        optRate1 = dataReduce(subData1, threshold)
    if len(subData2) < 5:
        optRate2 = 0.0
    else:
        optRate2 = dataReduce(subData2, threshold)
    # 计算总数据段的缩减率
    Rate = (optRate1 * len(subData1) + optRate2 * len(subData2)) / len(data)
    return Rate


# 根据不同误差阈值设置不同离散度进行分割的数据缩减算法
def dataSplitReduce_d(data, threshold):
    # 计算离散系数d=std/mean
    men = np.mean(data)
    sd = np.std(data)
    d = sd / men
    if threshold >= 1:
        Rate = dataReduce(data, threshold)
        return Rate
    elif threshold > 0.55 and threshold < 1:
        # 判断离散系数是否大于0.01,若大于，则表示需要分割，则求最佳分割点
        if d > 0.01:
            Rate = DataReduceByTtest(data)
        else:
            Rate = dataReduce(data, threshold)
        return Rate
    elif threshold > 0.45 and threshold <= 0.55:
        if d > 0.006:
            Rate = DataReduceByTtest(data)
        else:
            Rate = dataReduce(data, threshold)
        return Rate
    elif threshold > 0.35 and threshold <= 0.45:
        if d > 0.005:
            Rate = DataReduceByTtest(data)
        else:
            Rate = dataReduce(data, threshold)
        return Rate
    elif threshold > 0.25 and threshold <= 0.35:
        if d > 0.0045:
            Rate = DataReduceByTtest(data)
        else:
            Rate = dataReduce(data, threshold)
        return Rate
    else:
        if d > 0.004:
            Rate = DataReduceByTtest(data)
        else:
            Rate = dataReduce(data, threshold)
        return Rate


# 若原始的数据缩减率小于0.85则分割数据段，计算分割后的数据缩减算法
# def dataSplitReduce_r(insurance, threshold):
#     # 计算数据段的原始缩减率
#     r = dataReduce(insurance, threshold)
#     # 若原始数据缩减率r小于0.85，则分割数据段
#     if r < 0.85:
#         # 根据T检验求最佳分割点
#         T = []
#         num = len(insurance)
#         for split in range(1, num - 1):
#             x1 = insurance[:split]
#             x2 = insurance[split:]
#             n1 = len(x1)
#             n2 = len(x2)
#             mean_x1 = np.mean(x1)
#             mean_x2 = np.mean(x2)
#             std_x1 = np.std(x1)
#             std_x2 = np.std(x2)
#             sd = (math.sqrt((1.0 / n1) + (1.0 / n2))) * math.sqrt(
#                 ((n1 - 1.0) * (std_x1 ** 2) + (n2 - 1.0) * (std_x2 ** 2)) / (n1 + n2 - 2.0))
#             tep = math.fabs((mean_x1 - mean_x2) / sd)
#             k = split - 1
#             T.append([k, tep])
#
#         Tmax = T[0][1]
#         pos = 1
#         for i in range(1, len(T)):
#             if T[i][1] > Tmax:
#                 Tmax = T[i][1]
#                 pos = i + 1
#
#         # 分割数据为两个子数据段
#         subData1 = insurance[:pos]
#         subData2 = insurance[pos:]
#         # 两个子段分别进行缩减处理
#         if len(subData1) < 5:
#             optRate1 = 0.0
#         else:
#             optRate1 = dataReduce(subData1, threshold)
#         if len(subData2) < 5:
#             optRate2 = 0.0
#         else:
#             optRate2 = dataReduce(subData2, threshold)
#         # 计算总数据段的缩减率
#         Rate = (optRate1 * len(subData1) + optRate2 * len(subData2)) / len(insurance)
#
#         if Rate < r:
#             return r
#         else:
#             return Rate
#     else:
#         return r


# 不提前判断数据是否需要分割，直接分割后的数据缩减算法
# def dataSplitReduce_withoutD(insurance, threshold):
#     # 根据T检验求最佳分割点
#     T = []
#     num = len(insurance)
#     for split in range(1, num - 1):
#         x1 = insurance[:split]
#         x2 = insurance[split:]
#         n1 = len(x1)
#         n2 = len(x2)
#         mean_x1 = np.mean(x1)
#         mean_x2 = np.mean(x2)
#         std_x1 = np.std(x1)
#         std_x2 = np.std(x2)
#         sd = (math.sqrt((1.0 / n1) + (1.0 / n2))) * math.sqrt(
#             ((n1 - 1.0) * (std_x1 ** 2) + (n2 - 1.0) * (std_x2 ** 2)) / (n1 + n2 - 2.0))
#         tep = math.fabs((mean_x1 - mean_x2) / sd)
#         k = split - 1
#         T.append([k, tep])
#
#     Tmax = T[0][1]
#     pos = 1
#     for i in range(1, len(T)):
#         if T[i][1] > Tmax:
#             Tmax = T[i][1]
#             pos = i + 1
#     # print("pos: ", pos)
#     # 分割数据为两个子数据段
#     subData1 = insurance[:pos]
#     subData2 = insurance[pos:]
#     # 两个子段分别进行缩减处理
#     if len(subData1) < 5:
#         optRate1 = 0.0
#     else:
#         optRate1 = dataReduce(subData1, threshold)
#     if len(subData2) < 5:
#         optRate2 = 0.0
#     else:
#         optRate2 = dataReduce(subData2, threshold)
#     # 计算总数据段的缩减率
#     Rate = (optRate1 * len(subData1) + optRate2 * len(subData2)) / len(insurance)
#     return Rate


# CE数据集
def ce():
    data_path = r'E:\Desktop\scholar\edge insurance mana and compress\论文资料xmy\实验相关\paper_dev\dataset\CE.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for threshold in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
        print("threshold: ", threshold)
        for i in range(len(data)):  # 遍历每个周期数据
            # if i in [0, 46, 69, 152, 554, 651, 897, 1329]:
            # if i in [1, 2, 3, 45, 67, 888, 344, 893]:  # 测试
            if i in [1, 2, 3, 45, 67, 888, 344, 893, 0, 46, 69, 152, 554, 651, 897, 1329]:
                print("ce", i + 1, ": ------------------------------------")
                # split_reduce(insurance[i], splitpoint)
                r = dataReduce(data[i], threshold)
                print("rate: ", r)


# CP数据集
def cp():
    data_path = r'E:\Desktop\scholar\edge insurance mana and compress\论文资料xmy\实验相关\paper_dev\dataset\CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for threshold in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
        print("threshold: ", threshold)
        for i in range(len(data)):  # 遍历每个周期数据
            # if i in [0, 480, 818, 455, 998, 1255, 1999]:
            # if i in [1, 2, 233, 445, 675, 888, 344, 893]:  # 测试
            if i in [0, 480, 818, 455, 998, 1255, 1999, 1, 2, 233, 445, 675, 888, 344, 893]:
                print("cp", i + 1, ": ----------------------------------")
                # split_reduce(insurance[i], splitpoint)
                r = dataReduce(data[i], threshold)
                print("rate: ", r)


# TS数据集
def ts():
    data_path = r'E:\Desktop\scholar\edge insurance mana and compress\论文资料xmy\实验相关\paper_dev\dataset\TS1.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for threshold in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
        print("threshold: ", threshold)
        for i in range(len(data)):  # 遍历每个周期数据
            # if i in [3, 2, 31, 744, 88, 365, 1561, 1998]:
            # if i in [1, 2, 3, 45, 67, 54, 663, 893]:  # 测试
            if i in [1, 2, 3, 45, 67, 54, 663, 893, 3, 2, 31, 744, 88, 365, 1561, 1998]:
                print("ts", i + 1, ": ----------------------------------")
                # split_reduce(insurance[i], splitpoint)
                r = dataReduce(data[i], threshold)
                print("rate: ", r)


if __name__ == "__main__":
    data_path = r'E:\Desktop\scholar\edge insurance mana and compress\论文资料xmy\实验相关\paper_dev\dataset\CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    # for threshold in [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]:
    for threshold in [0.7]:
        rate = []
        total_rate = 0
        total_num = 0
        k = 0
        print("begin...")
        print("threshold: ", threshold)
        startTime = time.clock()
        for i in range(len(data)):
            if i >= 0 and i < 6:
                # print(k)
                rate_i = dataReduce(data[i], threshold)
                # rate_i = dataSplitReduce(insurance[i], threshold)
                # rate_i = dataSplitReduce_withoutD(insurance[i], threshold)
                # rate_i = dataSplitReduce_d(insurance[i], threshold)
                # rate_i = dataSplitReduce_r(insurance[i], threshold)
                rate.append(rate_i)
                total_rate = total_rate + rate_i
                k = k + 1
            if k > 7:
                break
        print("k: ", k)
        endTime = time.clock()
        total_rate = total_rate / k
        print(rate)
        print("totalRate:", "%7.4f" % total_rate)
        total_time = endTime - startTime
        print("total time: ", total_time / k)
