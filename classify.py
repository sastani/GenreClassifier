from __future__ import division
from tools.csv_tools import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd

def get_all_data(files):
    all_data = []
    for f in files:
        genre = read_mfcc_csv(f)
        for s in genre:
            all_data.append(s)
    return all_data

#cleans up data so only features and labels
def get_feats_labels(x, y):
    feats_only = []
    for d in x:
        feats_only.append(d[3:-2])
    return feats_only, y

def get_info_feats(x):
    all_songs = []
    feats_only = []
    for d in x:
        all_songs.append(d[0:3])
        feats_only.append(d[3:-2])
    return all_songs, feats_only

#scale features and seperate into input and output
def preprocess_and_seperate(data):
    s = []
    f = []
    x = []
    y = []
    for d in data:
        s.append(d[0:3])
        print(d[3:-2])
        f.append(d[3:-2])
        y.append(d[-1])
    f = np.array(f)
    f = preprocessing.scale(f)
    f = f.tolist()
    num_songs = len(s)
    for i in range(num_songs):
        feat_vec = f[i]
        song = s[i]
        x.append(song+feat_vec)
    return x, y

#split the data into training and test set
def process_and_split(data):
    x, y = preprocess_and_seperate(data)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20, stratify=y)
    x_train_feat, y_train = get_feats_labels(x_train, y_train)
    return x_train_feat, y_train, x_test, y_test

def validate(x_test, y_test, clf, misc):
    songs, feats = get_info_feats(x_test)
    num_songs = len(songs)
    count = 0
    y_pred = []
    misclassified_songs = []
    for i in range(num_songs):
        for x in range(len(feats[i])):
            feats[i][x] = float(feats[i][x])
        pred = clf.predict([feats[i]])
        pred = pred[0]
        y_pred.append(pred)
        row = []
        actual_label = y_test[i]
        if(actual_label == pred):
            count = count + 1
        else:
            row.append((songs[i])[2])
            row.append(pred)
            row.append(actual_label)
            misclassified_songs.append(row)
    cm = pd.crosstab(pd.Series(y_pred), pd.Series(y_test), rownames=['Predicted'], colnames=['Actual'], margins=True)
    accuracy = (count/num_songs)
    if(misc):
        return count, accuracy, cm, misclassified_songs
    else:
        return count, accuracy, cm








