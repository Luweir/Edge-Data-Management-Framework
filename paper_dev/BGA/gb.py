import numpy as np
import math
from BGA import beta

P0 = 0.85
L0 = 25

# start:1  end:60
def Tseries(x):
    T = []
    num = len(x)
    for split in range(1, num - 1):
        x1 = x[:split]
        x2 = x[split:]
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

    # t检验序列最大值
    # print("T: ", T)
    Tmax = T[0][1]
    pos = 1
    for i in range(1, len(T)):
        if T[i][1] > Tmax:
            Tmax = T[i][1]
            pos = i+1
    print("Tmax's pos: ", pos)
    # print("Tmax : ", Tmax)
    return pos

    # Eta = 4.19 * math.log(len(x)) - 11.54
    # Delta = 0.40
    # e = 1.0e-3
    # v = len(x) - 2
    # c = v / (v + pow(Tmax, 2))
    # PTmax = 1 - beta.beta2(Delta * Eta, Delta, c, e)
    # print("PTmax: ", PTmax)
    # if PTmax >= P0:
    #     return pos
    # else:
    #     return -1



# 计算数据三等分之后的平均T值，根据T值判断。//// 方法不可行
def Is_split_1(data):
    # 数据均分四等分
    q1 = int(len(data)/4)  # 四分之一处
    q2 = int(len(data)/2)  # 四分之二处
    q3 = int(len(data)/4 * 3)  # 四分之三处

    data1_pre = data[:q1]
    data1_tail = data[q1:]
    data2_pre = data[:q2]
    data2_tail = data[q2:]
    data3_pre = data[:q3]
    data3_tail = data[q3:]

    n1_pre = len(data1_pre)
    n1_tail = len(data1_tail)
    n2_pre = len(data2_pre)
    n2_tail = len(data2_tail)
    n3_pre = len(data3_pre)
    n3_tail = len(data3_tail)


    # 计算均值
    m1_pre = np.mean(data1_pre)
    m1_tail = np.mean(data1_tail)
    m2_pre = np.mean(data2_pre)
    m2_tail = np.mean(data2_tail)
    m3_pre = np.mean(data3_pre)
    m3_tail = np.mean(data3_tail)

    # 计算标准差
    sd1_pre = np.std(data1_pre)
    sd1_tail = np.std(data1_tail)
    sd2_pre = np.std(data2_pre)
    sd2_tail = np.std(data2_tail)
    sd3_pre = np.std(data3_pre)
    sd3_tail = np.std(data3_tail)

    # 计算三个Tmax值
    sd1 = (math.sqrt((1.0 / n1_pre) + (1.0 / n1_tail))) * math.sqrt(
        ((n1_pre - 1.0) * (sd1_pre ** 2) + (n1_tail - 1.0) * (sd1_tail ** 2)) / (n1_pre + n1_tail - 2.0))
    sd2 = (math.sqrt((1.0 / n2_pre) + (1.0 / n2_tail))) * math.sqrt(
        ((n2_pre - 1.0) * (sd2_pre ** 2) + (n2_tail - 1.0) * (sd2_tail ** 2)) / (n2_pre + n2_tail - 2.0))
    sd3 = (math.sqrt((1.0 / n3_pre) + (1.0 / n3_tail))) * math.sqrt(
        ((n3_pre - 1.0) * (sd3_pre ** 2) + (n3_tail - 1.0) * (sd3_tail ** 2)) / (n3_pre + n3_tail - 2.0))

    tp1 = math.fabs((m1_pre - m1_tail) / sd1)
    tp2 = math.fabs((m2_pre - m2_tail) / sd2)
    tp3 = math.fabs((m3_pre - m3_tail) / sd3)

    result = [tp1, tp2, tp3]
    print(result)

# 计算中间点的T值，根据PT值判断。/////方法不可行
def Is_split_2(data):
    split = int(len(data) / 2)
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
    T = math.fabs((mean_x1 - mean_x2) / sd)
    Eta = 4.19 * math.log(len(data)) - 11.54
    Delta = 0.40
    e = 1.0e-3
    v = len(data) - 2
    c = v / (v + pow(T, 2))
    PT = 1 - beta.beta2(Delta * Eta, Delta, c, e)
    print("PT: ", PT)
    # if PTmax >= P0:
    #     return 1
    # else:
    #     return -1





# 计算中间点的Z值，根据PZ值判断。
def Is_split_3(x):
    split = int(len(x)/2)
    x1 = x[:split]
    x2 = x[split:]
    n1 = len(x1)
    n2 = len(x2)
    mean_x1 = np.mean(x1)
    mean_x2 = np.mean(x2)
    std_x1 = np.std(x1)
    std_x2 = np.std(x2)
    sd = (std_x1 ** 2) / n1 + (std_x2 ** 2) / n2
    Z = (mean_x1 - mean_x2) / math.sqrt(sd)
    print("Z: ", Z)
