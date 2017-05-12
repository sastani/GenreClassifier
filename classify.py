import os
from tools.csv_tools import read_mfcc_csv
import numpy as np
from sklearn import preprocessing

def get_mfcc_files(dir):
    #get all the mfcc files in the genre subdirs
    genre_dirs = []
    for d in os.listdir(dir):
        path = os.path.join(dir, d)
        if os.path.isdir(path):
            genre_dirs.append(path)
    mfcc_files = []
    for d in genre_dirs:
        for file in os.listdir(d):
            if file == "genre_mfcc.csv":
                mfcc_files.append(os.path.join(d, file))
    return mfcc_files

def get_features(file):
    x, y = read_mfcc_csv(file)
    print(x)
    print(y)
    x = np.array(x)
    x = preprocessing.scale(x)
    return x, y

def get_all_input(files):
    x = []
    y = []
    for f in files:
        feat, label = get_features(f)
        x.append(feat)
        y.append(label)
    return x, y

def main(direc):
    mfcc_files = get_mfcc_files("/Users/sina/Documents/Dataset")
    data, labels = get_all_input(mfcc_files)
    print(data)
    print(labels)

if __name__ == '__main__':
    dir = raw_input("Input the directory of dataset: ")
    main(dir)
