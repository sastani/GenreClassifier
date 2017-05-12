import os
from pydub.audio_segment import AudioSegment
import csv
from id3tags import get_metadata
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import numpy as np

#convert to 30 second mono sample
def convert_wav(file, counter):
    filename, ext = os.path.splitext(file)
    wav_dir = os.path.dirname(file) + "/wav"
    if not os.path.exists(wav_dir):
        os.mkdir(wav_dir)
    ext = ext[1:]
    song = AudioSegment.from_file(file, ext)
    msecs = song.duration_seconds * 1000
    halfpoint = msecs/2
    thir_sec = song[halfpoint:(halfpoint+30000)]
    thir_sec = thir_sec.set_channels(1)
    new_filename = wav_dir + "/" + str(counter) + ".wav"
    thir_sec.export(new_filename, format="wav")
    return new_filename

# generate mfcc file for each 30 second wav sample
def create_mfcc(file):
    sample_rate, X = scipy.io.wavfile.read(file)
    m, mspec, spec = mfcc(X, fs=sample_rate)
    averaged_mfcc = np.mean(m[int(13 * 1 / 10):int(13 * 9 / 10)], axis=0)
    return averaged_mfcc

#generic function to append row to csv file
def write_row_to_csv(file, row):
    csv_file = open(file, "a")
    csv_write = csv.writer(csv_file)
    csv_write.writerow(row)

def write_row_and_close(file, row):
    csv_file = open(file, "a")
    csv_write = csv.writer(csv_file)
    csv_write.writerow(row)
    csv_file.close()



#convert to wav and rename files using 3bit numbers
def main(dir):
    dataset_file = dir + "/Dataset_SongList.csv"
    dataset_list = open(dataset_file, "a")
    csv_write = csv.writer(dataset_list)
    row = ["Artist", "Title", "Album", "Genre", "Filepath"]
    csv_write.writerow(row)
    dataset_list.close()
    for genre_subdir in os.listdir(dir):
        genre_path = dir + "/" + genre_subdir
        if os.path.isdir(genre_path):
            i = 0
            for file in os.listdir(genre_path):
                filepath = genre_path + "/" + file
                if not file.startswith('.') and os.path.isfile(filepath):
                    print(filepath)
                    count = "%03d" % i
                    new_file = convert_wav(filepath, count)
                    song_info = get_metadata(filepath)
                    song_info["filepath"] = new_file
                    row = [song_info["artist"], song_info["title"], song_info["album"], song_info["genre"],
                           song_info["filepath"]]
                    write_row_to_csv(dataset_file, row)
                    i += 1


if __name__ == "__main__":
    dir = raw_input("Input the directory of dataset: ")
    main(dir)









