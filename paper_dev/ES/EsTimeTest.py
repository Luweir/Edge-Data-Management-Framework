import ES.esmoothing as esmoothing
import time


# 以下标k开始分割
def split_data(data, k):
    s_pre = data[:k]
    s_tail = data[k:]
    return s_pre, s_tail


# 缩减算法的核心 时间复杂度O(n^2)
# 最坏情况下的缩减处理：alpha循环100次，分割点从4--len(insurance)
def dataReduce(data, threshold):
    alpha = 0.01  # alpha从0.01开始，按步长0.01开始变化增长
    while alpha < 1:
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
        alpha = alpha + 0.01


# 最佳情况下的时间测试  alpha一次，splitpoint一次
def dataReduce2(data):
    train, real = split_data(data, 12)
    next_n = len(real)  # 需要向后预测的数据的个数
    predict_n = []  # 存放预测的数据子段
    double_a, double_b = esmoothing.compute_double(0.01, train)  # 计算数据序列的a,b参数
    for nextT in range(1, next_n + 1):
        prediction = double_a[-1] + double_b[-1] * nextT
        predict_n.append(prediction)
    sum = 0.0  # 计算mape值
    for i in range(len(real)):
        sum = sum + abs((real[i] - predict_n[i]) / real[i])
    mape = sum * 100 / len(real)


# 测试恢复数据的时间开销
def recover(data, next_n):
    predict_n = []
    alpha = 0.02
    double_a, double_b = esmoothing.compute_double(alpha, data)  # 计算数据序列的a,b参数
    for nextT in range(1, next_n + 1):
        prediction = double_a[-1] + double_b[-1] * nextT
        predict_n.append(prediction)


if __name__ == "__main__":
    ts4 = [38.633, 38.535, 38.469, 38.379, 38.297, 38.223, 38.125, 38.062, 37.977, 37.969, 37.887, 37.902, 37.965,
           38.047, 38.18, 38.203, 38.367, 38.406, 38.457, 38.629, 38.633, 38.699, 38.801, 38.801, 38.828, 38.902,
           38.895, 38.969, 38.988, 39.055, 39.055, 39.055, 39.055, 39.121, 39.215, 39.215, 39.219, 39.227, 39.273,
           39.285, 39.293, 39.293, 39.273, 39.285, 39.375, 39.359, 39.375, 39.379, 39.367, 39.363, 39.441, 39.363,
           39.367, 39.457, 39.461, 39.461, 39.473, 39.441, 39.453, 39.461]
    cp456 = [1.577, 1.575, 1.577, 1.597, 1.596, 1.597, 1.601, 1.6, 1.596, 1.589, 1.592, 1.607, 1.612, 1.607, 1.609,
             1.605, 1.607, 1.613, 1.591, 1.587, 1.596, 1.609, 1.613, 1.61, 1.601, 1.596, 1.614, 1.595, 1.595, 1.588,
             1.572, 1.575, 1.579, 1.577, 1.575, 1.554, 1.544, 1.541, 1.547, 1.549, 1.559, 1.558, 1.565, 1.568, 1.569,
             1.572, 1.593, 1.598, 1.597, 1.593, 1.581, 1.581, 1.589, 1.585, 1.589, 1.611, 1.607, 1.605, 1.603, 1.612]
    cp1256 = [1.712, 1.712, 1.703, 1.722, 1.725, 1.732, 1.729, 1.729, 1.726, 1.724, 1.719, 1.714, 1.733, 1.734, 1.719,
              1.742, 1.739, 1.735, 1.77, 1.767, 1.782, 1.781, 1.787, 1.779, 1.786, 1.782, 1.766, 1.764, 1.786, 1.782,
              1.778, 1.763, 1.751, 1.76, 1.76, 1.758, 1.739, 1.724, 1.732, 1.737, 1.74, 1.734, 1.732, 1.74, 1.74, 1.739,
              1.722, 1.709, 1.71, 1.702, 1.722, 1.724, 1.729, 1.725, 1.739, 1.724, 1.723, 1.702, 1.737, 1.742]

    data = cp1256
    T = []
    for splitdata in range(4, 60):
        train = data[:splitdata]
        real = data[splitdata:]
        startTime = time.clock()
        for i in range(10000):
            recover(train, len(real))
        endTime = time.clock()
        atime = (endTime - startTime) / 10000
        T.append(atime)
        # print(time)
    print(T)
