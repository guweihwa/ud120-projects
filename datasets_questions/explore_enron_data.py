#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print "lenron_data=", enron_data
print "len(enron_data)=", len(enron_data)
print "# of features=", len(enron_data.items()[0][1])

cnt = 1
for f in enron_data.items()[0][1]:
    print cnt, "-", f
    cnt += 1

import sys
sys.path.append("../final_project/")

from poi_email_addresses import poiEmails

emails = poiEmails()

cnt = 0
tscnt = 0
ptcnt = 0
ecnt = 0
scnt = 0
mcnt = 0
pcnt = 0
for i in enron_data.items():
    if enron_data[i[0]]["poi"] == True:
        cnt += 1
        if enron_data[i[0]]["total_payments"] == "NaN":
            ptcnt +=1
        if enron_data[i[0]]["total_stock_value"] == "NaN":
            tscnt +=1
    #print i[0], ":", enron_data[i[0]]["email_address"]
    if enron_data[i[0]]["email_address"] in emails:
        ecnt += 1
    if "Prentice James".upper() in i[0]:
        print "total_stock_value of ", i[0], "=", enron_data[i[0]]["total_stock_value"]
    if "Colwell Wesley".upper() in i[0]:
        print "from_this_person_to_poi for ",  i[0], "=", enron_data[i[0]]["from_this_person_to_poi"]
    if "Skilling Jeffrey".upper() in i[0]:
        print "exercised_stock_options for ",  i[0], "=", enron_data[i[0]]["exercised_stock_options"]
    if "Lay Kenneth".upper() in i[0]:
        print "total_payments for ",  i[0], "=", enron_data[i[0]]["total_payments"]
    if "Skilling Jeffrey".upper() in i[0]:
        print "total_payments for ",  i[0], "=", enron_data[i[0]]["total_payments"]
    if "Fastow Andrew".upper() in i[0]:
        print "total_payments for ",  i[0], "=", enron_data[i[0]]["total_payments"]
    if enron_data[i[0]]["salary"] != "NaN":
        scnt += 1
    if enron_data[i[0]]["email_address"] != "NaN":
        mcnt += 1
    if enron_data[i[0]]["total_payments"] == "NaN":
        pcnt += 1

print "# of POI=", cnt, " ecnt=", ecnt, " scnt=", scnt, " mcnt=", mcnt
print "pcnt=", pcnt, "%pcnt=", pcnt/len(enron_data)
print "ptcnt=", ptcnt, "%ptcnt=", ptcnt/len(enron_data), " tscnt=", tscnt
