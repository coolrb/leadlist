import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import precision_recall_fscore_support
import numpy as np

def convertToFloat(lst):
    return np.array(lst).astype(np.float)

def fetchData(path):
    labels = []
    data = []
    f = open(path)
    csv_f = csv.reader(f)
    for row in csv_f:
        labels.append(convertToFloat(row[0]))
        data.append(convertToFloat(row[1:]))
    f.close()
    return np.array(data), np.array(labels)

def runForest(X_train, y_train):
    forest = RandomForestClassifier(n_estimators=90, random_state=42)
    forest.fit(X_train, y_train)
    return forest

def runSGD(X_train, y_train):
    sgd = SGDClassifier(n_iter=500, loss='modified_huber', penalty='elasticnet', random_state=42)
    sgd.fit(X_train, y_train)
    return sgd
 
def getScores(clf, X, y):
    predictions = clf.predict(X)
    scores = precision_recall_fscore_support(y, predictions, average='binary')
    return scores


# Import data
X_test, y_test = fetchData('data/test.csv')
X_train, y_train = fetchData('data/train.csv')

sgd = runSGD(X_train, y_train)
sgd_scores = getScores(sgd, X_test, y_test)
print 'SGD Scores: ', sgd_scores



