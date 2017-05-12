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
    features = []
    labels = []
    csvreader = csv.reader(csvfile, delimiter=',', )
    #get mfccs (training features) and genre (labels) from each row
    for row in csvreader:
        m = row[3:15]
        f = [abs(float(i))for i in m]
        l = row[16]
        features.append(f)
        labels.append(l)
    return features, labels

