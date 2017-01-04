#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def load_data(filepath):
    #load the dataset as a ndarray.
    dataset = np.loadtxt(open(filepath,"rb"),delimiter=",",skiprows=0)
    print("item {0} {1}".format("dimension is",dataset.shape))
    return dataset
