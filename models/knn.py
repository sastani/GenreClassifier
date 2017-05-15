from __future__ import division
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def train_model(x_train_feat, y_train):
    clf = KNeighborsClassifier()
    x_train_feat = np.array(x_train_feat)
    y_train = np.array(y_train)
    clf.fit(x_train_feat, y_train)
    return clf
