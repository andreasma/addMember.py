from plone import api
import csv

portal = api.portal.get()

users = api.user.get_users()

# write all current users in append mode to a csv-file
for f in users:
  id = f.getProperty('id')
  name = f.getProperty('fullname')
  email = f.getProperty('email')
  roles = api.user.get_roles(username = id)
  with open('currentmember.csv', 'ab') as csvfile:
    memberlist = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    memberlist.writerow([name,id,email,roles])