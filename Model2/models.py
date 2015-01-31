from mongoengine import *

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

class networking(Document):
	
	
	userA = IntField()
    	friendsof_A = ListField()
	
	


