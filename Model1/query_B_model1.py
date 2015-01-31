from models import tweets

count = 0
Retcount = 0
for obj in tweets.objects:
	count = count + 1
	print count
		if obj.Hashtags != ' ':
			Retcount = Retcount + item.Retcount
		
		else:
			continue

	
	if count == 7000000:
		break;

print Retcount
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'


