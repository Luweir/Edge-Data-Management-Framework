import numpy as np
import math
def z_test(x):
    Z = []
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
        sd = (std_x1**2)/n1 + (std_x2**2)/n2
        tep = (mean_x1 - mean_x2) / math.sqrt(sd)
        k = split - 1
        Z.append([k, tep])

    # Z检验序列最大值
    # print("T: ", Z)
    Zmax = Z[0][1]
    pos = 1
    for i in range(1, len(Z)):
        if Z[i][1] > Zmax:
            Zmax = Z[i][1]
            pos = i + 1
    print("Zmax's pos: ", pos)
    # print("Zmax : ", Zmax)
    return pos

