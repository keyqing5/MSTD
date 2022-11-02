"""
2022/10/12
According to the source code from https://github.com/zhanglabtools/MSTD/blob/master/src/MSTDlib/MSTD_v2.py
"""
import numpy as np


class MSTD():
    def __init__(self, input):
        self.matrix
        # hypeparameter

def input_file(input_file="simulation.txt",root_dir=None):
    input_file_dir = root_dir+input_file
    input_matrix = np.loadtxt(input_file_dir)
    return input_matrix