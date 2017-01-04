#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold import MDS
import os
from loadkit import load_data

def knn(kvalue=1,weight="uniform"):
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,"tempfile"))
    # print filepath
    trainset = load_data(os.path.join(filepath,"knn_train.csv"))
    testset = load_data(os.path.join(filepath,"knn_test.csv"))
    traintag = trainset[:,0]
    attrnum = trainset.shape[1]
    #testtag = testset[:,0]------------------------the order of mds and knn!!!!!
    mds = MDS(random_state=19)
    low_trainset = mds.fit_transform(trainset[:,2:attrnum])
    low_testset = mds.fit_transform(testset[:,2:attrnum])
    clf = KNeighborsClassifier(n_neighbors=kvalue,weights=weight)
    clf.fit(low_trainset,traintag)
    testpred = clf.predict(low_testset)
    # low_trainset = np.ndarray.tolist(np.column_stack((traintag, low_trainset)))
    # low_testset = np.ndarray.tolist(np.column_stack((testpred, low_testset)))
    traintag = np.ndarray.tolist(traintag)
    train_x = np.ndarray.tolist(low_trainset[:,0])
    train_y = np.ndarray.tolist(low_trainset[:,1])
    testpred = np.ndarray.tolist(testpred)
    test_x = np.ndarray.tolist(low_testset[:,0])
    test_y = np.ndarray.tolist(low_testset[:,1])
    low_trainset = {'tag':traintag,'train_x':train_x,'train_y':train_y}
    low_testset = {'tag':testpred,'test_x':test_x,'test_y':test_y}
    compresseddata = {'traindata':low_trainset,'testdata':low_testset}
    return compresseddata

