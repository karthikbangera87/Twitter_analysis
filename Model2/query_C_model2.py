from models import users_new,tweets_new,networking
import time
import os
import re


start = time.time()

fp = open('Friendlist_model2','w+')


maximum = 0
count = 0
friends = []
id_name_dict={}
for userobj in users_new.objects:
	
	count = count + 1
	print count
	id_name_dict[userobj.userid] = userobj.username
	if userobj.friendcount >= maximum:
		maximum = userobj.friendcount
		max_friendcount_id = userobj.userid
	
	else:
		continue

print 'The user with the maximum friend count is',max_friendcount_id
print 'The user has',maximum,'friends'

for nwobj in networking.objects:
	if max_friendcount_id == nwobj.userA:
		friends = nwobj.friendsof_A
		break;	

for item in friends:
	if item in id_name_dict:	
		fp.write(id_name_dict[item])
		fp.write('\n')
	else:
		continue


fp.close()
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'



