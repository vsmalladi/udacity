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

#  Follow The Money
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

# Unfilled features
print enron_data['FASTOW ANDREW S'].values()

 # Dealing With Unfilled Features
# Finding POIs In The Enron Data
salary = 0
email = 0
for k in enron_data.keys():
    if enron_data[k]["salary"] != 'NaN':
        salary += 1
    if enron_data[k]["email_address"] != 'NaN':
        email += 1

print salary
print email

# Missing POIs 1 (Optional)
total = 0
for k in enron_data.keys():
    if enron_data[k]["total_payments"] == 'NaN':
        total += 1

print total/float(len(enron_data.keys())) * 100

# Missing POIs 2 (Optional)
total_pois = 0
for k in enron_data.keys():
    if enron_data[k]["poi"] == 1:
        if enron_data[k]["total_payments"] == 'NaN':
            total_pois += 1

print total_pois/float(pois) * 100
