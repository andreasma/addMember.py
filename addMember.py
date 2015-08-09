from plone import api
import csv
import transaction


portal = api.portal.get()

# import new member from a new csv-file 'newuserdata.csv' into Plone
# the csv-file has to be comma separated with the order: fullname,email,username
with open('newuserdata.csv', 'rb') as f:
    f.seek(0)
    reader = csv.reader(f)
    for row in reader:
        api.user.create(username=row[2], email=row[1], properties ={'fullname':row[0]})

transaction.commit()

# get all current users from the Plone instance
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