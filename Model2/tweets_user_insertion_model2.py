from models import tweets_new,users_new
import time
import os
import re
start = time.time()

file_tracker = []
object_count=[]
object_tracker = 0
userchange = 0
tweetchange = 0
testing = 0
attriblist = ['Type','Origin','Text','URL','ID','Time','RetCount','Favorite','MentionedEntities','Hashtags']



for root,dirs,files in os.walk('/Volumes/MAC1/tweets',topdown=False):
	print ' Inside the tweets folder'
	for name in files:
		file_tracker.append(name)
fp = open('/Volumes/MAC1/users/users.txt','r')
for line in fp:

       
        line = line.split('\t')
	tweet_tracker = []
	if line[0] in file_tracker:
		print 'Opening' , line[0]
		#if name == line[0]: 
		print ' Opening tweet files for', line [0]
		fileobj = open(os.path.join(root,name))
		count = 0
		data=[]
		tweetobj = 'tweetobject'+str(tweetchange)
		for tweetline in fileobj:

	
	
       			if tweetline =='***\n' or tweetline =='***':
        	
				if count == 11:
			
                        		tweetobj = tweets_new(
					Type=data[0],
                        		origin=data[1],
                        		text=data[2],
                        		URL=data[3],
                        		ID=data[4],
                        		time=data[5],
                        		Retcount=data[6],
                        		Favorite=data[7],
                        		MentionedEntities=data[8],
                        		Hashtags=data[9])
                        		data=[]
                        		count = 0
					tweet_tracker.append(tweetobj)
                        		tweetchange = tweetchange+1
                        		tweetobj = 'tweetobject'+str(tweetchange)
					
				else:
					count = count + 1
               
			

			else:
				
				check = tweetline.partition(':')
				if check[0] not in attriblist:
					continue
				else:

					data.append(check[2].rstrip('\n'))                                                 
                			count = count + 1
		
				
	Userobj = 'UserObj'+ str(userchange)
        line[7] = re.sub('[^A-Za-z0-9]+',' ',line[7]).strip()
        Userobj = users_new(
        userid = int(line[0]),
        username = line[1],
        friendcount = int(line[2]),
        followercount = int(line[3]),
        statuscount = int(line[4]),
        Favoritecount = int(line[5]),
        location = line[7],
	tweets = tweet_tracker)
	
	object_count.append(Userobj)
	object_tracker = object_tracker + 1
        if object_tracker == 302:
                print 'Entering 10 objects'
                bulkobj = users_new.objects.insert(object_count)
                print 'Bulk objects saved', testing
                testing = testing + 1
                object_tracker = 0
                object_count =[]

	userchange = userchange+1
        Userobj = 'UserObj'+str(userchange)


end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

