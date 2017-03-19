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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of people
print len(enron_data.keys())

# Number of features
print len(enron_data['METTS MARK'].keys())

# Finding POIs In The Enron Data
pois = 0
for k in enron_data.keys():
    if enron_data[k]["poi"] == 1:
        pois += 1

print pois

# Query The Dataset 1
print enron_data['PRENTICE JAMES']['total_stock_value']

# Query The Dataset 2
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# Query The Dataset 3
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
