from models import tweets
import time
import os
start = time.time()
change = 0
attriblist = ['Type','Origin','Text','URL','ID','Time','RetCount','Favorite','MentionedEntities','Hashtags']


for root,dirs,files in os.walk('/Volumes/MAC1/tweets',topdown=False):
	for name in files:
		fp = open(os.path.join(root,name))
		#fp = open('test','r')
		count = 0
		#attrib_count= 0
		data=[]
		obj = 'Object'+str(change)
		for line in fp:

	
	
       			if line =='***\n' or line =='***':
        	
		
				if count == 11:
			
                        		obj = tweets(
								UserID = name,
								Type=data[0],
                        		origin=data[1],
                        		text=data[2],
                        		URL=data[3],
                        		ID=data[4],
                        		time=data[5],
                        		Retcount=data[6],
                        		Favorite=data[7],
                        		MentionedEntities=data[8],
                        		Hashtags=data[9]).save()
                        		data=[]
                        		count = 0
                        		change = change+1
                        		obj = 'Object'+str(change)
					print obj
				else:
			
					count = count + 1
               
			

			else:
				
				check = line.partition(':')
				if check[0] not in attriblist:
					continue
				else:

					data.append(check[2].rstrip('\n'))                                                 
                			count = count + 1


 
end = time.time()
elapsed = end - start
print 'Time taken:',elapsed,'seconds'

