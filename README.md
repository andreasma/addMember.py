# addMember.py

This Python script adds members from a csv-file to a Plone Content Management System (CMS) instance. In the second step it gets all members from that site and appand them to another csv-file.
The csv-input file is currently hard coded to 'newuserdata.csv' and the output file (to append the current user data) is hard coded to 'currentmember.csv'. You need the first file in the basic directory of your instance.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' you could run this script with:

`./bin/instance -O testing run addMember.py`
