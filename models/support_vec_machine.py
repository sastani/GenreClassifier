from __future__ import division
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from classify import *
import numpy as np


def grid_search(x, y, kernel):
    trainData, testData, trainLabels, testLabels = train_test_split(x, y, test_size=0.20, random_state=0, stratify=y)
    parameters = {}
    k = [kernel]
    costs = [0.01, 0.1, 1, 10, 100]
    gammas = [0.001, 0.01, 0.1, 1]
    degrees = [1, 2, 3]
    parameters['kernel'] = k
    parameters['C'] = costs
    parameters['gamma'] = gammas
    parameters['degree'] = degrees
    svr = svm.SVC()
    classifier_gs = GridSearchCV(svr, parameters, cv=5)
    classifier_gs.fit(trainData, trainLabels)
    return classifier_gs.best_params_, classifier_gs.score(testData, testLabels)

def gs_for_eachkernel(d):
    x, y = preprocess_and_seperate(d)
    outfile = open("svm_output.txt", "w")
    kernels = ['linear', 'poly', 'rbf']
    for k in kernels:
        params, acc = grid_search(x, y, k)
        outfile.write("[INFO] grid search best parameters: {}".format(params))
        outfile.write('\n')
        outfile.write("[INFO] grid search accuracy: {:.2f}%".format(acc * 100))
        outfile.write('\n')

def train_model(x_train_feat, y_train):
    clf = svm.SVC(C=1, gamma=0.1, degree=1, kernel='rbf')
    x_train_feat = np.array(x_train_feat)
    y_train = np.array(y_train)
    clf.fit(x_train_feat, y_train)
    return clf

def main():
    mfcc_files = get_mfcc_files("/Users/sina/Documents/Dataset")
    d = get_all_data(mfcc_files)
    gs_for_eachkernel(d)


if __name__== '__main__':
    main()
