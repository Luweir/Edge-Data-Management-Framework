import matplotlib.pyplot as plt
import numpy as np

def showdata(x, y, title):
    plt.figure(figsize=(24, 10), dpi=80)
    plt.plot(x, y, color='blue', label="insurance value")
    plt.title('TS'+ str(title))
    plt.xticks(x)
    plt.show()

if __name__ == "__main__":
    data_path = r'data/TS1.txt'  # 设置数据路径
    data = np.loadtxt(data_path)
    total_data = []
    for i in range(len(data)):
        if i == 56 or i == 780 or i == 1186:
            total_data = data[i].tolist()
            x = np.arange(1, len(total_data) + 1)
            showdata(x, total_data, i+1)
        elif i > 1186:
            break












