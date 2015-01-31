from models import users,networking
import time
import os
import re

start = time.time()


#Before adding a follower to User 10489322
print 'Before adding a follower to User 10489322'
for nwobj in networking.objects:
	if nwobj.userA == 10489322:
		print nwobj.friendsof_A
		break;

#adding follower 82580813 to user 10489322
for nwobj in networking.objects:
	if nwobj.userA == 10489322:
		nwobj.friendsof_A.append(82580813) 
		nwobj.save()
		break;
#updating followercount and friendcounts in user profiles
for userobj in users.objects:
		if userobj.userid == 82580813:
			 userobj.followercount = userobj.followercount + 1
			 userobj.save()
			 break;

for userobj in users.objects:
		if userobj.userid == 10489322:
			userobj.friendcount = userobj.friendcount + 1
			userobj.save()
			break;
		




end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

