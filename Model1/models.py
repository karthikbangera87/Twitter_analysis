from mongoengine import *
connect('tweetsdata')


class tweets(Document):
	
	UserID = StringField()
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

class networking(Document):
	
	userA = IntField()
    	friendsof_A = ListField()
    

class users(Document):
	
	userid = IntField()
    	username = StringField()
    	friendcount = IntField()
	followercount = IntField()
	statuscount = IntField()
	Favoritecount = IntField()
	account_age = StringField()
	location = StringField()
	

