from sklearn.naive_bayes import GaussianNB
import numpy as np

def train_model(x_train_feat, y_train):
    clf = GaussianNB()
    x_train_feat = np.array(x_train_feat)
    y_train = np.array(y_train)
    clf.fit(x_train_feat, y_train)
    return clf

