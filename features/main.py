import os
from features.convert import convert_wav
from tools.csv_tools import *
from features.extract import create_mfcc
from tools.id3tags import get_metadata

def gen_features(dir, dlist):
    i = 0
    for genre_subdir in os.listdir(dir):
        genre_path = dir + "/" + genre_subdir
        #create a file of mfccs for all songs in that genre
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
                    #write song title and metadata to dataset songlist
                    write_row_to_csv(dlist, row)
                    row = [tags["artist"], tags["title"],
                           file_id]
                    for x in m:
                        row.append(x)
                    row.append(tags["genre"])
                    #write artist and song title, along with mfccs to mfcc file
                    write_row_to_csv(mfcc_file, row)
                    i += 1

#convert to wav and rename files using 3bit numbers
def main(dir):
    #create dataset song list and write headers to csv file
    dataset_file = dir + "/Dataset_SongList.csv"
    row = ["Artist", "Title", "Album", "Genre", "Filepath"]
    write_row_and_close(dataset_file, row)
    gen_features(dir, dataset_file)


if __name__ == "__main__":
    dir = raw_input("Input the directory of dataset: ")
    main(dir)