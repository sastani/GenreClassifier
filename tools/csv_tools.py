import csv

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

def read_mfcc_csv(file):
    csvfile = open(file, "rb")
    genre = []
    csvreader = csv.reader(csvfile, delimiter=',', )
    #get mfccs (training features) and genre (labels) from each row
    for row in csvreader:
        song =  []
        song_info = row[0:3]
        for i in song_info:
            song.append(i)
        m = row[3:16]
        for i in m:
            mfcc = (float(i))
            song.append(mfcc)
        label = row[16]
        song.append(label)
        genre.append(song)
    return genre

