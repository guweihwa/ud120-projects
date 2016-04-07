#!/usr/bin/python

### %matplotlib inline
### %run enron_outliers.py

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

for item in data_dict.items():
     if data_dict[item[0]]["salary"] != "NaN" and data_dict[item[0]]["salary"] > 10**6:
            print item[0], " salary=", data_dict[item[0]]["salary"]
            if data_dict[item[0]]["salary"] > 10**7:
                outlier = item[0]

data_dict.pop(outlier, 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")

matplotlib.pyplot.show()
