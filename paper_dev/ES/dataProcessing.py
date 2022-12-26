import numpy as np
import math
import paper_dev.ES.esmoothing as esmoothing
import time


# 以下标k开始分割
def split_data(data, k):
    s_pre = data[:k]
    s_tail = data[k:]
    return s_pre, s_tail


# 计算平均绝对百分比误差（Mean Absolute Percentage Error，MAPE）
def mape(real, predict):
    sum = 0.0
    for i in range(len(real)):
        sum = sum + abs((real[i] - predict[i]) / real[i])
    result = sum * 100 / len(real)
    return result


# 计算均方根误差（Mean Square Root Error (MSRE)）
def msre(real, predict):
    sum = 0.0
    for i in range(len(real)):
        sum = sum + math.sqrt((real[i] - predict[i]) ** 2)
    result = sum / len(real)
    return result


# 选择指数平滑预测  n ：几阶指数平滑 ,nextn : 向后预测第 nextn 个数据
def esmooth(n, alpha, data, nextn):
    if n == 1:
        sigle = esmoothing.compute_single(alpha, data)
        prediction = alpha * data[-1] + (1 - alpha) * sigle[-1]
        return prediction
    elif n == 2:
        double_a, double_b = esmoothing.compute_double(alpha, data)
        prediction = double_a[-1] + double_b[-1] * nextn
        return prediction
    elif n == 3:
        triple_a, triple_b, triple_c = esmoothing.compute_triple(alpha, data)
        prediction = triple_a[-1] + triple_b[-1] * nextn + triple_c[-1] * (nextn ** 2)
        return prediction


# 根据历史数据data，向后预测连续next_n个数据
def predict(n, alpha, data, next_n):
    predict_n = []  # 预测的数据
    for i in range(1, next_n + 1):
        predict_num = esmooth(n, alpha, data, i)
        predict_n.append(predict_num)
    return predict_n


# 计算预测误差是否在预测值之内
def Is_qualified(real, predict, threshold):
    err = mape(real, predict)
    if err >= threshold:
        return 0
    else:
        return 1


# 找到符合阈值的数据子集，二分法切割数据   insurance:总数据
def subdata(n, alpha, data, threshold):
    low = 1  # 最少1个数据
    high = len(data)  # 数据最多这么多个
    result = high
    while high - low > 1:
        split_point = int((high + low) / 2)
        train, real = split_data(data, split_point)  # 将数据划分为两部分：一部分训练，另一部分可恢复（用于比对预测误差）
        next_n = len(real)  # 预测接下来next_n个值
        # 如果划分之后数据训练子集小于3，则不再继续划分
        if len(train) <= 3:
            return result
        else:
            predict_num = predict(n, alpha, train, next_n)
            if Is_qualified(real, predict_num, threshold):
                result = split_point
                high = split_point - 1
            else:
                low = split_point + 1
    return result  # 返回找到子集最佳划分点


# 简单粗暴方法找数据子集
def subdata_2(n, alpha, data, threshold):
    result = len(data)
    for split_point in range(4, len(data)):  # 分割点从4到数据的长度
        train, real = split_data(data, split_point)  # insurance[0:split_point]训练集；insurance[split+1:end]真实数据
        next_n = len(real)  # 真实数据长度
        predict_num = predict(n, alpha, train, next_n)  # 使用训练集进行预测
        if Is_qualified(real, predict_num, threshold):
            return split_point
        else:
            continue
    # 如果每一次划分的误差都大于阈值，则说明该数组无法预测，返回切割点：data长度
    return result


# 计算缩减率 C=缩减的数据量/总数据量data
def reduce_rate(n, alpha, data, threshold):
    id = subdata_2(n, alpha, data, threshold)
    train, real = split_data(data, id)
    rate = len(real) / len(data)
    return rate


# 循环alpha（指数平滑系数）找最优的缩减率
def optimal_rate(n, data, threshold):
    alpha = 0.01
    rate = []
    while alpha < 1:
        rate_i = reduce_rate(n, alpha, data, threshold)
        rate.append(rate_i)
        alpha = alpha + 0.01
    opt_rate = max(rate)
    return opt_rate


if __name__ == "__main__":
    data_path = r'../dataset/CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    # print(insurance)
    rate = []
    total_rate = 0  # 总压缩率
    total_num = 0  # 原始数据总长度
    n = 2  # 二次指数平滑
    threshold = 1  # MAPE误差阈值   1-MAPA
    start_time = time.time()
    print("begin...")
    # for i in range(len(insurance)):
    for i in range(20):  # 以五个数据集做测试
        rate_i = optimal_rate(n, data[i], threshold)
        rate.append(rate_i)
        print(i + 1)
        total_rate = total_rate + rate_i * len(data[i])
        total_num = total_num + len(data[i])
    end_time = time.time()
    total_rate = total_rate / total_num
    print(rate)
    print("totalRate:", "%6.3f" % total_rate)
    total_time = end_time - start_time
    print("total time: ", total_time / len(data))

    ################ 固定alpha值 #####################################
    # 固定alpha值
    # data_path = r'insurance\TS1.txt'  # 设置数据路径
    # insurance = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    # # print(insurance)
    # rate = []
    # total_rate = 0
    # total_num = 0
    # n = 2
    # threshold = 0.7
    # start_time = time.time()
    # k = 0
    # for i in range(len(insurance)):
    #     # if i < 99:
    #     #     continue
    #     rate_i = reduce_rate(n, 0.31, insurance[i], threshold)
    #     rate.append(rate_i)
    #     k = k + 1
    #     print(k)
    #     if i == 5:
    #         break
    #     total_rate = total_rate + rate_i * len(insurance[i])
    #     total_num = total_num + len(insurance[i])
    # end_time = time.time()
    # total_rate = total_rate / total_num
    # print(rate)
    # print("totalRate:", "%6.3f" % total_rate)
    # total_time = end_time - start_time
    # print("total time: ", total_time / k)
