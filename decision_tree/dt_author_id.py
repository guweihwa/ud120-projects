#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
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
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

print "number of features in train=",  len(features_train[0])

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"

print "answer10=", pred[10]
print "answer26=", pred[26]
print "answer50=", pred[50]

import numpy as np
print "# of 1's(sum)=", np.sum(pred)
print "# of 1's(count_nonzero)=", np.count_nonzero(pred)

import collections
print "# of 1's(Counter)=", collections.Counter(pred)
# of 1's(Counter)= Counter({0: 881, 1: 877})

print "len(pred)=", len(pred), " len(labes_test)=", len(labels_test)

from sklearn.metrics import accuracy_score
print "accuracy_score:", (accuracy_score(labels_test, pred))



#########################################################
