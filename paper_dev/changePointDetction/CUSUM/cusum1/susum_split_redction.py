import Cusum
import ES.dataset_split_reduction as dsr
import ES.split_segment_reduce as ssr
import numpy as np
import time


# 以cusum的上偏移量最值作为分割点
def findSplitPoint(data):
    k = Cusum.buildk(data, Cusum.utils.mean(data))
    shvals, slvals, hlist, nhlist = Cusum.cusum(data, k, 20)
    splitpoint = shvals.index(max(shvals))
    return splitpoint

# 缩减处理
def dataSet_reduction_forCUSUM(data, threshold):
    if dsr.Is_split(data):
        # 根据CUSUM计算分割点
        splitpoint = findSplitPoint(data)
        # 计算分割后的数据缩减率
        rate = ssr.split_reduce(data, splitpoint, threshold)
    else:
        rate = ssr.reductionRate(data, threshold)
    return rate


if __name__ == "__main__":
    data_path = r'E:\WorkSpace_xmy\paper_dev\dataset\CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    # print(insurance)
    threshold = 0.8
    rate = []
    total_rate = 0
    total_num = 0
    start_time = time.time()
    k = 0
    print("begin...")
    for i in range(len(data)):
        k = k + 1
        print(k)
        rate_i = dataSet_reduction_forCUSUM(data[i], threshold)
        rate.append(rate_i)
        # total_rate = total_rate + rate_i * len(insurance[i])
        total_rate = total_rate + rate_i
        # total_num = total_num + len(insurance[i])
        if k == 100:
            break
    end_time = time.time()
    # total_rate = total_rate / total_num
    total_rate = total_rate / k
    print(rate)
    print("totalRate:", "%7.4f" % total_rate)
    total_time = end_time - start_time
    print("average time: ", total_time / k)



