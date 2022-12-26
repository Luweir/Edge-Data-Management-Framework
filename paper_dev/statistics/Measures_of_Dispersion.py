import numpy as np

# 计算离散度
def dispersion(data):
    men = np.mean(data)
    sd = np.std(data)
    return sd/men

# CE数据集
def ce():
    data_path = r'E:\WorkSpace_xmy\paper_dev\dataset\CE.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for i in range(len(data)):  # 遍历每个周期数据
        # if i in [0, 46, 69, 152, 554, 651, 897, 1329]:
        if i in [1, 2, 3, 45, 67, 888, 344, 893]:     # 测试
            dis = dispersion(data[i])
            print("ce", i+1, ": ", dis)


# CP数据集
def cp():
    data_path = r'E:\WorkSpace_xmy\paper_dev\dataset\CP.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for i in range(len(data)):  # 遍历每个周期数据
        # if i in [0, 480, 818, 455, 998, 1255, 1999]:
        if i in [1, 2, 233, 445, 675, 888, 344, 893]:  # 测试
            dis = dispersion(data[i])
            print("cp", i+1, ": ", dis)


# TS数据集
def ts():
    data_path = r'E:\WorkSpace_xmy\paper_dev\dataset\TS1.txt'  # 设置数据路径
    data = np.loadtxt(data_path)  # 用numpy读取数据  [[第一行],[第二行],[第三行],...,[第n行]]  2205*60
    for i in range(len(data)):  # 遍历每个周期数据
        # if i in [3, 2, 31, 744, 88, 365, 1561, 1998]:
        if i in [1, 2, 3, 45, 67, 54, 663, 893]:  # 测试
            dis = dispersion(data[i])
            print("ts", i+1, ": ", dis)


if __name__ == "__main__":
    ce()
    cp()
    ts()
