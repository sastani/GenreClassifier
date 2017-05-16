from __future__ import division
from tools.csv_tools import *
import numpy as np
from sklearn import preprocessing
import pandas as pd

def get_all_data(files):
    all_data = []
    for f in files:
        genre = read_mfcc_csv(f)
        for s in genre:
            all_data.append(s)
    return all_data

#split data into input and output numpy arrays
#concatenate mfccs for each frame
#scale features
def preprocess_and_seperate(data):
    y = []
    all_feats = []
    for song in data:
        mfccs_in_song = song[0]
        oned_mfccs_in_song = []
        for frame in mfccs_in_song:
            for m in frame:
                oned_mfccs_in_song.append(m)
        all_feats.append(oned_mfccs_in_song)
        label = song[-1]
        y.append(label)
    all_feats = check_size(all_feats)
    feat = np.array(all_feats)
    feat = preprocessing.scale(feat)
    y = np.array(y)
    return feat, y

def validate(x_test, y_test, clf):
    num_test = len(y_test)
    count = 0
    y_pred = []
    for i in range(num_test):
        x = x_test[i].reshape(1,-1)
        pred = clf.predict(x)
        pred = pred[0]
        y_pred.append(pred)
        actual_label = y_test[i]
        if(actual_label == pred):
            count = count + 1
    cm = pd.crosstab(pd.Series(y_pred), pd.Series(y_test), rownames=['Predicted'], colnames=['Actual'], margins=True)
    accuracy = (count/num_test)
    return count, accuracy, cm

def check_size(list):
    min_size = min(len(i) for i in list)
    for i in range(len(list)):
        if len(list[i]) > min_size:
            list[i] = list[i][:min_size]
    return list




