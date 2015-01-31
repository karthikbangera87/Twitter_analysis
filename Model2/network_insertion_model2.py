from models import networking
import time
import os
import re

check = 1
start = time.time()
change = 0
filenamelist=[]
directory = '/Volumes/MAC1/network/'
object_count = []
object_tracker = 0


	

obj = 'NwObj'+ str(change)
friendlist=[]

for root,dirs,files in os.walk('/Volumes/MAC1/network',topdown=False):
                for name in files:
                        filenamelist.append(name)

for item in filenamelist:
	counter = 0
	nwtest = open(directory+item,'r')	
	for nwline in nwtest:  	
	
		if counter == 0:
			validity = nwline.split('\t')
			prev = int(validity[0])
		


		nwline = nwline.split('\t')
		if prev == int(nwline[0]):
			prev = int(nwline[0])
			friendlist.append(int(nwline[1])) 
			counter = counter + 1
		
		else:	
			obj = networking()
			obj.userA = prev
			obj.friendsof_A = friendlist

			object_count.append(obj)
			object_tracker = object_tracker + 1
        		if object_tracker == 100:
                		print 'Entering 100 objects'
				print object_count
                		bulkobj = networking.objects.insert(object_count)
                		print 'Bulk objects saved',check
                		check = check + 1
                		object_tracker = 0
                		object_count =[]
			
			change = change+1
        		obj = 'NwObj'+ str(change)
			friendlist = []
			prev = int(nwline[0])
			friendlist.append(int(nwline[1]))



	print 'Exiting out the file reading last line and saving'
	
	obj = networking()
	obj.userA = prev
        obj.friendsof_A = friendlist
	object_count.append(obj)
	print object_count
        bulkobj = networking.objects.insert(object_count)
	print 'Remaining objects saving'
	object_tracker = 0
        object_count =[]
	change = change+1
        obj = 'NwObj'+ str(change)
        friendlist = []



end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

	

