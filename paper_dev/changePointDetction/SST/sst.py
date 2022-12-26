import banpei
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ES.dataset_split_reduction as dsr
import ES.split_segment_reduce as ssr
import time

def showdata(x, y):
    plt.figure(figsize=(24, 10), dpi=80)
    plt.plot(x, y, color='blue', label="insurance")
    # plt.title('ts1999')
    plt.xticks(x)
    plt.show()

# 找分割点
def findSplitPoint(data):
    model = banpei.SST(w=4, L=2)
    results = model.detect(data, is_lanczos=True)
    re = results.tolist()
    splitpoint = re.index(max(re))
    return splitpoint


# 缩减处理
def dataSet_reduction_forSST(data, threshold):
    if dsr.Is_split(data):
        # 根据CUSUM计算分割点
        splitpoint = findSplitPoint(data)
        # 计算分割后的数据缩减率
        rate = ssr.split_reduce(data, splitpoint, threshold)
    else:
        rate = ssr.reductionRate(data, threshold)
    return rate


if __name__ == "__main__":
    data_path = r'E:\WorkSpace_xmy\paper_dev\dataset\CE.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    # print(insurance)
    threshold = 0.5
    rate = []
    total_rate = 0
    total_num = 0
    start_time = time.time()
    k = 0
    print("begin...")
    for i in range(len(data)):
        k = k + 1
        print(k)
        rate_i = dataSet_reduction_forSST(data[i], threshold)
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
    print("average time: ", total_time / k)


