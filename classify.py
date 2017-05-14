from tools.csv_tools import read_mfcc_csv
import numpy as np
from sklearn.model_selection import KFold, train_test_split
from tools.get_files import get_mfcc_files
from sklearn import preprocessing


'''
def get_features(file):
    x = np.array(x)
    y = np.array(y)
    x = preprocessing.scale(x)
    z = 0
    genre = []
    return x, y, z
    '''
#cleans up data so only features and labels
def get_all_data(files):
    all_data = []
    for f in files:
        genre = read_mfcc_csv(f)
        for s in genre:
            all_data.append(s)
    return all_data

def get_feats_labels(x, y):
    feats_only = []
    for d in x:
        feats_only.append(d[3:16])
    return x, y

def preprocess_and_split(data):
    s = []
    f = []
    x = []
    y = []
    for d in data:
        s.append(d[0:3])
        f.append(d[3:16])
        y.append(d[16])
    f = np.array(f)
    f = preprocessing.scale(f)
    f = f.tolist()
    num_songs = len(s)
    for i in range(num_songs):
        feat_vec = f[i]
        song = s[i]
        x.append(song+feat_vec)
    return x, y

def create_folds(x, y):
    kf = KFold(n_splits=5, shuffle=True)
    train = []
    test = []
    i = 1
    for train, test in kf.split(X=x, y=y):
        train_set = x[train]
        train_set_labels = y[train]
        test_set = x[test]
        test_set_labels = y[test]
        train_set_features = []
        test_set_features = []
        # get only the features (not the song data)
        for l in train_set:
            train_set_features.append(l[3:-1])
        for k in test_set:
            test_set_features.append(k[3:-1])

        i = i + 1

#split the data into training and test using hold out method
def create_hold_out(data, size):
    x, y = preprocess_and_split(data)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=size, random_state=42)
    x_train_feat, y_train = get_feats_labels(x_train, y_train)
    return x_train_feat, y_train, x_test, y_test

def main(direc):



if __name__ == '__main__':
    #dir = raw_input("Input the directory of dataset: ")
    main("a")
