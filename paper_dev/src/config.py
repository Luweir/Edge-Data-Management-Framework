# -*- coding: utf-8 -*-
# @Create Time    : 2019-03-27 12:33
# @Author  : Xingqiang Chen
# @Software: PyCharm

import argparse
import os

root_dir = '/Users/xingqiangchen/Desktop/2019-02-22/'

data_path = os.path.join(root_dir, 'insurance')
data_check_path = os.path.join(root_dir,'data_check')
data_prod_path = os.path.join(root_dir ,'data_prod')

if not os.path.exists(data_check_path):
    os.makedirs(data_check_path)

if not os.path.exists(data_prod_path):
    os.makedirs(data_prod_path)

data_name = ['10.csv', '56.csv', '64.csv', '72.csv', '84.csv',
             '11.csv', '56_0.csv', '64_0.csv', '73.csv', '85.csv',
             '12.csv', '57.csv', '65.csv', '74.csv', '86.csv',
             '40.csv', '60.csv', '66.csv', '77.csv', '87.csv',
             '45.csv', '60_0.csv', '67.csv', '78.csv', '89.csv',
             '50.csv', '61.csv', '68.csv', '80.csv',
             '51.csv', '62.csv', '69.csv', '81.csv',
             '52.csv', '63.csv', '70.csv', '82.csv',
             '55.csv', '63_2.csv', '71.csv', '83.csv']

# RULSIF Settings
settings = {'--alpha': 0.5, "--sigma": None, '--lambda': 1.5, '--kernels': 100, '--folds': 5, '--debug': None}
# insurance load
# make Hankel Matrix
# sample length 150s  n = 1500
n = 150
# sequence length 3s equals 30*100ms
before_Times = 30

# define event length
event_length = 1000

# detection aggressive events settings
first_time = False
only_evaluation = True

# define feature name parameters
data_feature_list = ['Acceleration', 'Velocity', 'Yaw_Rate']

start = 0
end = 20  # in total there are 4471
MPI = True
restart = False

# test for insurance checking
test_debug = False
if test_debug:
    data_name = data_name[0:1]
else:
    pass


def parse_arguments(argv):
    """
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--int_start', type=str, help='the start of detection task.', default='0')
    parser.add_argument('--int_end', type=str, help='the end of detection task.', default='')
    parser.add_argument('--MPI', type=bool, help='if or not use MPI.', default=False)
    parser.add_argument('--restart', type=bool, help='if or not restart of task', default=False)

    return parser.parse_args(argv)

