
"""
git checkout origin/master -- scripts/scrape.py
"""

#!/usr/bin/env python

import csv
import sys
import os
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from main.models import City, State, CityCas

from unidecode import unidecode
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

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

    city = unidecode(row['name'])

    print city

    city = unidecode(row['name'])
    session = cluster.connect() 
    city2 = CityCas(name=city)
    city2.save()

    cluster.shutdown()