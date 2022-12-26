import os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, wait

import numpy as np
import pandas as pd

from src.config import data_check_path, data_prod_path, \
    settings, before_Times, n, MPI, restart, start, end, data_feature_list
from src.rulsif import RULSIF
import time


def calculate_divergence_score(X_reference, X_test, settings):
    """
    :param X_reference:
    :param X_test:
    :param settings:
    :return:
    """
    estimator = RULSIF(settings=settings)

    # Train the model
    estimator.train(X_reference, X_test)

    divergence_score = estimator.apply(X_reference, X_test)
    options = {'--debug': 1}
    # estimator.show(displayName='try',options=options)

    return divergence_score


def result(data, n, settings):
    result = []
    for i in range(0, len(data) - n):
        Y_ref = data[i:i + n]
        Y_tes = data[i + 1:i + n + 1]
        # print(Y_ref)
        # print(Y_tes)
        score = calculate_divergence_score(Y_ref, Y_tes, settings)
        result.append([i + n, score])
    return result


def test():
    settings = {'--alpha': 0.5, "--sigma": None, '--lambda': None, '--kernels': 100, '--folds': 5, '--debug': 1}
    estimator = RULSIF(settings=settings)
    X_reference = np.array([[-327.538995, 1060.88410, -5135.11159],
                            [-6079.76383, 4540.07072, 4683.89186],
                            [-519.485848, -65.427245, -460.108594],
                            [4968.97172, 3051.50683, -102.050991],
                            [-5501.4825, -1951.72530, -44.1323003]])
    X_test = np.array([[4968.97172, 3051.50683, -102.050991],
                       [-5501.4825, -1951.72530, -44.1323003],
                       [2872.91368, -555.026187, 1582.54918],
                       [4968.97172, 3051.50683, -102.050991],
                       [-5501.4825, -1951.72530, -44.1323003]])
    # Train the model
    estimator.train(X_reference, X_test)
    divergence_score = estimator.apply(X_reference, X_test)
    options = {'--debug': 1}
    estimator.show(displayName='try', options=options)
    print("divergence_score...: ", divergence_score)


if __name__ == "__main__":
    ce47 = [19.515, 19.567, 19.646, 19.85, 19.852, 19.824, 19.75, 19.683, 19.475, 19.639, 19.693, 19.696, 19.714, 19.76,
            19.727, 19.67, 19.398, 19.643, 19.359, 19.359, 19.612, 19.671, 19.63, 19.63, 19.669, 19.339, 19.157, 19.063,
            19.009, 18.894, 19.001, 18.908, 19.129, 19.137, 19.088, 18.994, 18.779, 18.759, 18.675, 18.795, 18.785,
            18.911, 19.012, 19.209, 19.276, 19.279, 18.994, 19.163, 19.168, 19.219, 19.468, 19.445, 19.727, 19.696,
            19.696, 19.67, 19.437, 19.483, 19.357, 19.527]

    testdata = np.array(
        [[19.515, 19.567, 19.646, 19.85, 19.852, 19.824], [19.398, 19.643, 19.359, 19.359, 19.612, 19.671],
         [19.009, 18.894, 19.001, 18.908, 19.129, 19.137], [19.696, 19.67, 19.437, 19.483, 19.357, 19.527]])

    data = np.array(
        [[19.515, 19.567, 19.646, 19.85, 19.852, 19.824, 19.75, 19.683, 19.475, 19.639, 19.693, 19.696, 19.714, 19.76,
          19.727, 19.67, 19.398, 19.643, 19.359, 19.359, 19.612, 19.671, 19.63, 19.63, 19.669, 19.339, 19.157, 19.063,
          19.009, 18.894, 19.001, 18.908, 19.129, 19.137, 19.088, 18.994, 18.779, 18.759, 18.675, 18.795, 18.785,
          18.911, 19.012, 19.209, 19.276, 19.279, 18.994, 19.163, 19.168, 19.219, 19.468, 19.445, 19.727, 19.696,
          19.696, 19.67, 19.437, 19.483, 19.357, 19.527]])
    # print(insurance.shape)
    data1 = data.T  # 转置变成60行一列
    # print(data2[2:5])

    n = 15
    settings = {'--alpha': 0.5, "--sigma": None, '--lambda': 0.5, '--kernels': 100, '--folds': 3, '--debug': 1}
    start_time = time.time()
    res = result(data1, n, settings)
    end_time = time.time()
    print("result: ", res)
    print("time: ", end_time - start_time)
