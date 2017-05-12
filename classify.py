from processaudio import create_mfcc, write_row_to_csv
from id3tags import get_metadata, get_artist_title
import pickle
from processaudio import convert_wav
import os
from sklearn import svm


def gen_features(dir, dlist):
    i = 0
    for genre_subdir in os.listdir(dir):
        genre_path = dir + "/" + genre_subdir
        mfcc_file = genre_path + "/genre_mfcc.csv"
        if os.path.isdir(genre_path):
            #create wav subdirectory if doesn't exist
            files = os.listdir(genre_path)
            for f in files:
                file = genre_path + "/" + f
                if ".mp3" in f:
                    count = "%03d" % i
                    wav_file = convert_wav(file, count)
                    m = create_mfcc(wav_file)
                    tags = get_metadata(file)
                    tags["filepath"] = file
                    file_id = count + ".wav"
                    row = [tags["artist"], tags["title"], tags["album"], tags["genre"],
                           tags["filepath"], file_id]
                    write_row_to_csv(dlist, row)
                    row = [tags["artist"], tags["title"],
                           file_id]
                    for x in m:
                        row.append(x)
                    print(row)
                    write_row_to_csv(mfcc_file, row)
                    i += 1


def main(direc):
    dataset_file = direc + "Dataset_SongList.csv"
    row = ["Artist", "Title", "Album", "Genre", "Filepath", "File ID"]
    write_row_to_csv(dataset_file, row)
    gen_features(direc, dataset_file)

if __name__ == '__main__':
    dir = raw_input("Input the directory of dataset: ")
    main(dir)
