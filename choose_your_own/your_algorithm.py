#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from IPython.display import Image, display
from time import time

def testClassifier(clf):

    print "number of features in train=",  len(features_train[0])

    t0 = time()
    clf.fit(features_train, labels_train)
    tt = time()

    prettyPicture(clf, features_test, labels_test)
    #output_image("test.png", "png", open("test.png", "rb").read())
    display(Image("test.png"))

    print "training time:", round(tt-t0, 3), "s"

    t1 = time()
    pred = clf.predict(features_test)
    print "predict time:", round(time()-t1, 3), "s"

    #print "answer10=", pred[10]
    #print "answer26=", pred[26]
    #print "answer50=", pred[50]

    import numpy as np
    #print "# of 1's(sum)=", np.sum(pred)
    print "# of 1's(count_nonzero)=", np.count_nonzero(pred)

    import collections
    print "# of 1's(Counter)=", collections.Counter(pred)
    # of 1's(Counter)= Counter({0: 881, 1: 877})

    print "len(pred)=", len(pred), " len(labes_test)=", len(labels_test)

    from sklearn.metrics import accuracy_score
    print "accuracy_score:", (accuracy_score(labels_test, pred))

    return


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
print "\n===> GaussianNB"
testClassifier(clf)

from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=10000.0)
print "\n===> SVC"
testClassifier(clf)

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
print "\n===> DecisionTreeClassifier"
testClassifier(clf)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=4)
print "\n===> KNeighborsClassifier"
testClassifier(clf)

from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100)
print "A\n===> daBoostClassifier"
testClassifier(clf)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
print "\n===> RandomForestClassifier"
testClassifier(clf)

#try:
    #prettyPicture(clf, features_test, labels_test)
#except NameError:
#    pass
