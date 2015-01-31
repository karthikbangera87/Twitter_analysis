from mongoengine import *
import time
import os
import re
start = time.time()

connect('tweetsdata_newmodel')

class tweets_new(EmbeddedDocument):


        Type = StringField()
        origin = StringField()
        text = StringField()
        URL = StringField()
        ID = StringField()
        time = StringField()
        Retcount = IntField()
        Favorite = StringField()
        MentionedEntities = StringField()
        Hashtags = StringField()

class users_new(Document):


        userid = IntField()
        username = StringField()
        friendcount = IntField()
        followercount = IntField()
        statuscount = IntField()
        Favoritecount = IntField()
        account_age = StringField()
        location = StringField()
	tweets = ListField(EmbeddedDocumentField(tweets_new))


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


