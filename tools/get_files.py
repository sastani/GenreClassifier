import os

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
            if "mfcc.csv" in file:
                mfcc_files.append(os.path.join(d, file))
    return mfcc_files