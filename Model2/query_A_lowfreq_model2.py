from mongoengine import *
import time
import os
import re
start = time.time()


search_term = 'apple'
count = 0
fp = open('model2_random.txt','w+')
for obj in users_new.objects:
    count = count + 1
    print count
    for item in obj.tweets:
        if search_term in item.text:
            fp.write(str(obj.userid))
            fp.write('\n')
        
        else:
            continue

    
    if count == 400000:
        break;

fp.close()
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

