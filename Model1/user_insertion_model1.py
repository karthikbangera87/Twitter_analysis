from models import users
import time
import os
import re

check = 1
start = time.time()
change = 0
object_count = []
object_tracker = 0

fp = open('/Volumes/MAC1/users/users.txt','r')
obj = 'UserObj'+ str(change)


for line in fp:
	
	line = line.split('\t')
	obj = users()
	obj.userid = int(line[0])
        obj.username = line[1]
        obj.friendcount = int(line[2])
        obj.followercount = int(line[3])
        obj.statuscount = int(line[4])
        obj.Favoritecount = int(line[5])
        obj.account_age = line[6]
	line[7] = re.sub('[^A-Za-z0-9]+',' ',line[7]).strip()
	obj.location = line[7]
	
	
	object_count.append(obj)
	
	object_tracker = object_tracker + 1
	if object_tracker == 604:
		print 'Entering 604 objects'
		bulkobj = users.objects.insert(object_count)
		print 'Bulk objects saved',check
		check = check + 1
		object_tracker = 0
		object_count =[]
		
	
	change = change+1
        obj = 'UserObj'+str(change)


end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

