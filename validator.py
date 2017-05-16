from classify import *
from tools.get_files import get_mfcc_files
from models import support_vec_machine, knn, gaussian_nb

def kfold_cv(k):
    mfcc_files = get_mfcc_files("/Users/sina/Documents/Dataset")
    d = get_all_data(mfcc_files)
    files = ["./svm.csv", "./knn.csv", "./gaussian_nb.csv"]
    sums = [0, 0, 0]
    x, y = preprocess_and_seperate(d)
    for i in range(k):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20, stratify=y)
        #train a svm classifer, and then test
        trained_clf = support_vec_machine.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf, False)
        write_to_csv(files[0], c, a, cm)
        sums[0] = sums[0] + a
        #train a knn classifier, and then test
        trained_clf = knn.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf, False)
        write_to_csv(files[1], c, a, cm )
        sums[1] = sums[1] + a
        #train a NB classifier, and then test
        trained_clf = gaussian_nb.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf, False)
        write_to_csv(files[2], c, a, cm )
        sums[2] = sums[2] + a
    for i in range(len(files)):
        f = files[i]
        mean = "Mean accuracy: " + str(sums[i]/k)
        write_csv(f, mean)

kfold_cv(10)
