#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)

### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
#words_file = "./word_data_overfit.pkl"
#authors_file = "./email_authors_overfit.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

print "origin features_train.shape", features_train.shape

### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

### your code goes here
print "features_train.shape", features_train.shape
print "len(features_train)", len(features_train)

from sklearn import tree
clf = tree.DecisionTreeClassifier()  #min_samples_split=2)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print "test accuracy_score:", (accuracy_score(labels_test, pred))

importances = clf.feature_importances_
most_important = max(importances)
print "most_important={0}, len(importances)={1}".format(most_important, len(importances))

index = -1
for i in range(len(importances)):
    if importances[i] == most_important:
        index = i

    if importances[i] >= 0.2:
        print "features_train[0][{0}]={1}]  importances[{0}]={2}".format(i, features_train[0][i], importances[i])

print vectorizer.get_feature_names()[index]
