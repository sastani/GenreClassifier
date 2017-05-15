import csv

def write_to_csv(file, c, a, cm):
    csv_file = open(file, "a")
    csv_file.write("Total correct: %s\n" % (c))
    csv_file.write("Accuracy: %s\n" % (a))
    csv_file.close()
    cm.to_csv(file, header=True, index=True, sep=',', mode='a')
    csv_file = open(file, "a")
    csv_file.write("\n")
    csv_file.close()

def write_csv(file, d):
    csv_file = open(file, "a")
    csv_file.write(d)

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
    i = 0
    for row in csvreader:
        song = []
        song_info = row[0:3]
        for i in song_info:
            song.append(i)
        m = row[3:-2]
        song.append(m)
        label = row[-1]
        song.append(label)
        genre.append(song)
    return genre

