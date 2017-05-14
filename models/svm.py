from sklearn import svm
from sklearn.model_selection import GridSearchCV
from classify import *

def grid_search(x, y, kernel):
    trainData, testData, trainLabels, testLabels = train_test_split(
    x, y, test_size=0.20, random_state=42)
    parameters = {}
    k = [kernel]
    costs = [0.01, 0.1, 1, 10, 100]
    gammas = [0.001, 0.01, 0.1, 1]
    degrees = [1, 2, 3]
    parameters['kernel'] = k
    parameters['C'] = costs
    parameters['gamma'] = gammas
    parameters['degree'] = degrees
    svr = svm.SVC()
    classifier_gs = GridSearchCV(svr, parameters, cv=5)
    classifier_gs.fit(x, y)
    return classifier_gs.best_params_, classifier_gs.score(testData, testLabels)

def cv_gridsearch(d):
    x, y = preprocess_and_split(d)
    feat, label = get_feats_labels(x, y)
    outfile = open("svm_output.txt", "w")
    kernels = ['linear']
    for k in kernels:
        params, acc = grid_search(feat, label, k)
        outfile.write("[INFO] grid search best parameters: {}".format(params))
        outfile.write('\n')
        outfile.write("[INFO] grid search accuracy: {:.2f}%".format(acc * 100))

def train_svm(d):
    svm_clf = svm.SVC(C=1.0, gamma=1, kernel='rbf')
    x_train_feat, x_test, y_train, y_test = create_hold_out(d)
    svm_clf.fit(x_train_feat, y_train)


def main():
    mfcc_files = get_mfcc_files("/Users/sina/Documents/Dataset")
    d = get_all_data(mfcc_files)
    cv_gridsearch(d)
    x_train, x_test, y_train, y_test = create_hold_out(.20)



if __name__== '__main__':
    main()
