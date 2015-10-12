#!/usr/bin/env python

import csv
import sys
import os
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from main.models import City, State


# states = State.objects.all()

# for state in states:
# print state.name

print os.path.abspath(__file__)

# print os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cities.csv"
# print "%s/%s" % (dir_name, file_name)

# print os.path.join(dir_name, file_name)

cities_csv = os.path.join(dir_name, file_name)

csv_file = open(cities_csv, 'r')

reader = csv.DictReader(csv_file)
for row in reader:
    new_city, created = City.objects.get_or_create(name=row['city'])
    new_city.zip_code = row['zip_code']
    new_city.lat = row['latitude']
    new_city.lon = row['longitude']
    new_city.county = row['county']
    try:
        new_city.save()
    except:
        print "city does not have required date"    
    # new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    # new_capital.lat = row['latitude']
    # new_capital.lon = row['longitude']
    # new_capital.coun = row['county']
    try:
        new_city.state = State.objects.get(abbrev=row['state'])
    except:
        print "puerto rico?"
    try:
        new_city.save()
    except:
        print "----------could not save ---------------------------"    