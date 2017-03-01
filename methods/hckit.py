#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
# from sklearn.cluster import AgglomerativeClustering
# from sklearn.manifold import MDS
import plotly.plotly as pp
from plotly.tools import FigureFactory as ff

import os
from loadkit import load_data

def hc():
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,"tempfile"))
    dataset = load_data(os.path.join(filepath,"hc_data.csv"))
    names = dataset[:,0]
    arrnum = dataset.shape[1]
    fig = ff.create_dendrogram(dataset[:,2:arrnum],labels=names)
    fig['layout'].update({'width':810,'height':600})
    pp.plot(fig,filename='dendrogram')
    return 'success'
