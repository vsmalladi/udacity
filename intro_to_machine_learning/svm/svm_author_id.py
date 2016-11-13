#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(kernel='linear')
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
pred = clf.predict(features_test)

# Accurary
t0 = time()
accuracy = clf.score(features_test,labels_test)
print "training time:", round(time()-t0, 3), "s"
print accuracy

# Reduce to 1% of traning data
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='linear')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

# Change to rbf
clf = SVC(kernel='rbf')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

# Change the values of C (10,100,1000,10000)

## 10
clf = SVC(kernel='rbf', C=10)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

## 100
clf = SVC(kernel='rbf', C=100)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

## 1000
clf = SVC(kernel='rbf', C=1000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

## 10000
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy


# RBF with fulll training data set
features_train, features_test, labels_train, labels_test = preprocess()
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = clf.score(features_test,labels_test)
print accuracy

# Reduce to 1% training and use prediction of (10, 26, 50)
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print pred[10]
print pred[26]
print pred[50]

# How many are  predicted to be Chris
features_train, features_test, labels_train, labels_test = preprocess()
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
pred.describe()
print pred.sum()
#########################################################
