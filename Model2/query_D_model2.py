from models import user_new,tweets_new,networking
import time
import os
import re

start = time.time()


#adding follower 55094428 to user 10501112
for nwobj in networking.objects:
	if nwobj.userA == 10501112:
		nwobj.friendsof_A.append(55094428) 
		nwobj.save()
		break;
#updating followercount and friendcounts in user profiles
for userobj in users_new.objects:
		if userobj.userid == 55094428:
			 userobj.followercount = userobj.followercount + 1
			 userobj.save()
			 break;

for userobj in users_new.objects:
		if userobj.userid == 10501112:
			userobj.friendcount = userobj.friendcount + 1
			userobj.save()
			break;
		

end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

