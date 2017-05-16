from classify import *
from tools.get_files import get_mfcc_files
from models import support_vec_machine, knn, gaussian_nb
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from models.support_vec_machine import gs_for_eachkernel

def kfold_cv(x, y, k):
    files = ["./svm.csv", "./knn.csv", "./gaussian_nb.csv"]
    sums = [0, 0, 0]
    for i in range(k):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20, stratify=y)
        #train a svm classifer, and then test
        trained_clf = support_vec_machine.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[0], c, a, cm)
        sums[0] = sums[0] + a
        #train a knn classifier, and then test
        trained_clf = knn.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[1], c, a, cm )
        sums[1] = sums[1] + a
        #train a NB classifier, and then test
        trained_clf = gaussian_nb.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[2], c, a, cm )
        sums[2] = sums[2] + a
    for i in range(len(files)):
        f = files[i]
        mean = "Mean accuracy: " + str(sums[i]/k)
        write_csv(f, mean)

def kfold_models(x, y, k):
    files = ["./svm.csv", "./knn.csv", "./gaussian_nb.csv"]
    skf = StratifiedKFold(n_splits=k, random_state=None, shuffle=False)
    folds = skf.split(x, y)
    sums = [0, 0, 0]
    for train_index, test_index in folds:
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # train a svm classifer, and then test
        trained_clf = support_vec_machine.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[0], c, a, cm)
        sums[0] = sums[0] + a
        # train a knn classifier, and then test
        trained_clf = knn.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[1], c, a, cm)
        sums[1] = sums[1] + a
        # train a NB classifier, and then test
        trained_clf = gaussian_nb.train_model(x_train, y_train)
        c, a, cm = validate(x_test, y_test, trained_clf)
        write_to_csv(files[2], c, a, cm)
        sums[2] = sums[2] + a
    for i in range(len(files)):
        f = files[i]
        mean = "Mean accuracy: " + str(sums[i] / k)
        write_csv(f, mean)

def main():
    mfcc_files = get_mfcc_files("/Users/sina/Documents/Dataset")
    d = get_all_data(mfcc_files)
    x, y = preprocess_and_seperate(d)
    kfold_models(x, y, 10)
    gs_for_eachkernel(d)


if __name__ == '__main__':
    main()


