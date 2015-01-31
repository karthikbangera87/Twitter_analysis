from models import users_new,tweets_new
import time
import os
import re
start = time.time()


count = 0
Retcount = 0
for obj in users_new.objects:
	count = count + 1
	print count
	for item in obj.tweets:
		if item.Hashtags != ' ':
			Retcount = Retcount + item.Retcount
		
		else:
			continue

	
	if count == 400000:
		break;

print Retcount
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'


