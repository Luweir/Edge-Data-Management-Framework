import numpy as np
import BGA.Z_test as Ztest
import BGA.gb as Ttest
import ES.split_segment_reduce as ssr
import time


# 计算离散度
def dispersion(data):
    men = np.mean(data)
    sd = np.std(data)
    return sd / men


# 如果离散度dis大于0.1，则分割
def Is_split(data):
    dis = dispersion(data)
    if dis >= 0.01:
        return True
    else:
        return False


# 根据Z检验的结果分割计算缩减率
def dataSet_reduction_forZ(data, threshold):
    if Is_split(data):
        # 根据Z检验计算分割点
        splitpoint = Ztest.z_test(data)
        # 计算分割后的数据缩减率
        rate = ssr.split_reduce(data, splitpoint, threshold)
    else:
        rate = ssr.reductionRate(data, threshold)
    return rate


# 根据T检验的结果分割计算缩减率
def dataSet_reduction_forT(data, threshold):
    if Is_split(data):
        # 根据T检验计算分割点
        splitpoint = Ttest.Tseries(data)
        # 计算分割后的数据缩减率
        rate = ssr.split_reduce(data, splitpoint, threshold)
    else:
        rate = ssr.reductionRate(data, threshold)
    return rate


# 计算数据集的总体缩减率（每段数据分割后的缩减率）
def dataSetRate():
    data_path = r'E:\Desktop\Scholar\Edge Data Mana and compress\论文资料xmy\实验相关\paper_dev\dataset\CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    threshold = 0.2
    rate = []
    total_rate = 0
    total_num = 0
    start_time = time.time()
    k = 0
    print("begin...")
    for i in range(len(data)):
        k = k + 1
        print(k)
        rate_i = dataSet_reduction_forT(data[i], threshold)
        rate.append(rate_i)
        # total_rate = total_rate + rate_i * len(insurance[i])
        total_rate = total_rate + rate_i
        # total_num = total_num + len(insurance[i])
    end_time = time.time()
    # total_rate = total_rate / total_num
    total_rate = total_rate / k
    print(rate)
    print("totalRate:", "%7.4f" % total_rate)
    total_time = end_time - start_time
    print("total time: ", total_time / k)


if __name__ == "__main__":
    dataSetRate()
