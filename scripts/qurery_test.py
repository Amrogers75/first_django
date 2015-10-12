#!/usr/bin/env python

import csv
import sys
import os
import django
django.setup()

from main.models import State, StateCapital

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


# state = State.objects.get(pk=153)
# #print state.abbrev
# states = State.objects.all().order_by('-pop')
# print states

# for state in states:
# print state.name


# states = State.objects.all().exclude(name_contains='N')
# states = State.objects.all().exclude(name_icontains='N')


# for state in states:
# 	print state.name

# states = State.objects.all().values('name', 'pop')

# for state in states:
# 	print state['name'] #[0]

# states = State.objects.all().values_list('name', 'abbrev', 'pk')

# print states

# for state in  states:
# print state[2]
# print state[0]
# print "State Name: %s, State Abbreviation: %s" % (state[0], state[1])

# states = State.objects.all().values_list('name', 'abbrev', 'pop')

# for name, abbrev, pop, in states:
# "Name:{0}, Abbrev:{1}, Pop{1}".fomat(abbrev, pop, name)

# states = State.objects.all().exclude(name_startswith='N').filter(pop__gte='500000').order_by(-pop).values_list('name', 'pop')

# print states

# for  state in states :
# print "%s %s" % (state.name, state.pop)

# print "%s %s" % (state['0'], state['1'])

# states = State.objects.filter(name__in=states_list)

# print states

# state = State.objects.get(name='Alabama')

# print state.statecapital_set.all()

state = State = objects.get(pk=153)
state2 = State = objects.get(pk=194)
state3 = State = objects.get(pk=195)
state4 = State = objects.get(pk=196)

cap = StateCapital.objects.get(pk=1)
cap2 = StateCapital.objects.get(pk=2)
cap3 = StateCapital.objects.get(pk=3)


print cap.name
print state.name

# state.statecapital_set.remove.add(cap)
cap.state.add(state)
cap.state.add(state2)
cap.state.add(state3)
cap.state.add(state4)


state.statecapital_set.add(cap)
state.statecapital_set.add(cap2)
state.statecapital_set.add(cap3)

# state.statecapital_set.all()

state.statecapital_set.all()

# for state in states
# print "%s %s" % (state.name, state.statecapital.name)
