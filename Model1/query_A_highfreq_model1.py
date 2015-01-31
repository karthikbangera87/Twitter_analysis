from models import tweets

start = time.time()
fp = open('query_good.txt','w+')
count = 1
search_term = 'good'
for obj in tweets.objects:
	
	print count
	count = count + 1	
	if search_term in obj.text:
		fp.write(obj.UserID)
		fp.write('\n')

	if count ==7000000:
		break;


fp.close()
 
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

