#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import MDS

import os
from loadkit import load_data

def kmeans(kvalue=1,seed=1):
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,"tempfile"))
    dataset = load_data(os.path.join(filepath,"kmeans_data.csv"))
    datatag = dataset[:,0]
    attrnum = dataset.shape[1]
    mds = MDS(random_state=19)
    low_dataset = mds.fit_transform(dataset[:,2:attrnum])
    kcluster = KMeans(n_clusters=kvalue,random_state=seed).fit(low_dataset)
    clusterlabel = kcluster.labels_
    centroids = kcluster.cluster_centers_

    datatag = np.ndarray.tolist(datatag)
    data_x = np.ndarray.tolist(low_dataset[:,0])
    data_y = np.ndarray.tolist(low_dataset[:,1])
    clusterlabel = np.ndarray.tolist(clusterlabel)
    centroids_x = np.ndarray.tolist(centroids[:,0])
    centroids_y = np.ndarray.tolist(centroids[:,1])
    low_dataset = {'tag':datatag,'data_x':data_x,'data_y':data_y,'clusterlabel':clusterlabel}
    centroids = {'tag':'centroids','centroids_x':centroids_x,'centroids_y':centroids_y}
    compresseddata = {'dataset':low_dataset,'centroids':centroids}
    return compresseddata
