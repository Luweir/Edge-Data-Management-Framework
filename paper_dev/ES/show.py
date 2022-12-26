import matplotlib.pyplot as plt
import numpy as np


def showdata():
    plt.figure(figsize=(12, 8), dpi=80)
    cpx = [99.1, 99.2, 99.3, 99.4, 99.5, 99.6, 99.7, 99.8, 99.9]
    cpy = [0.7498, 0.6770, 0.5929, 0.5033, 0.4070, 0.3040, 0.1839, 0.0928, 0.0272]
    plt.plot(cpx, cpy, color='yellow', linestyle='-', marker='>', markersize='8', label="CP")
    cey = [0.8364, 0.7859, 0.7254, 0.6458, 0.5508, 0.4351, 0.3045, 0.1165, 0.0457]
    plt.plot(cpx, cey, color='blue', linestyle='-', marker='s', markersize='5', label="CE")
    tsy = [0.9327, 0.9325, 0.9323, 0.9318, 0.9311, 0.9154, 0.8348, 0.6917, 0.4153]
    plt.plot(cpx, tsy, color='red', linestyle='-', marker='*', markersize='8', label="TS")
    cpys = [0.8230, 0.770, 0.6897, 0.5998, 0.4995, 0.3865, 0.2472, 0.1321, 0.0461]
    plt.plot(cpx, cpys, color='y', linestyle='--', marker='>', markersize='8', label="CP*")
    ceys = [0.8718, 0.8458, 0.8018, 0.7235, 0.6230, 0.4946, 0.3465, 0.1907, 0.0574]
    plt.plot(cpx, ceys, color='b', linestyle='--', marker='s', markersize='5', label="CE*")
    tsys = [0.9329, 0.9327, 0.9322, 0.9317, 0.9310, 0.9156, 0.8351, 0.6923, 0.4161]
    plt.plot(cpx, tsys, color='r', linestyle='--', marker='*', markersize='8', label="TS*")

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,
               ncol=6, mode="expand", borderaxespad=0.)
    # plt.title('ts1999')
    plt.grid(True)
    # plt.scatter(cpx, cpy)
    plt.xlabel("Forecast Accuracy (MAPA)")
    plt.ylabel("Reduction rate(RC)")
    plt.ylim((0, 1))
    # plt.xticks()
    plt.show()


if __name__ == "__main__":
    showdata()
