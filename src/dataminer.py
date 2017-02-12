# Jace Robinson
# 3-6-16
# CS 3250 Dataminer of twitter
# Example from http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
# Goal is to extract tweets from super tuesday 2016 in JSON format

import tweepy
import json
import time
import tweepy
from tweepy import OAuthHandler

# Candidate information
# trump: @realdonaldtrump 25073877
# cruz: @tedcruz 23022687
# rubio: @marcorubio 15745368
# kasich: @JohnKasich 18020081
# clinton: @HillaryClinton 1339835893
# sanders: @BernieSanders 216776631
# cnn: @cnn 759251
# foxnews: @foxnews 1367531
# huffingtonpost: @HuffingtonPost 14511951
# cnbc: @CNBC 20402945
# newyorktimes: @nytimes 807095

# Setup keys
consumer_key = 'TStFM6M58QWW4NRQhMXbfoOtu'
consumer_secret = 'gxdKyoTaIzo7SDhokEnJceWkRjJ7zMNy0CHkj71ugKvu4huBMx'
access_token = '4847203607-RIofAER99syXmoPt7yhXN6itYF4O8LSlTossrXT'
access_secret = 'aimNQwAqoXSRw3zg41mEDhYaLhTRSQeqnxOu1KARErDOk'
directory = 'Sanders/'
twitterAccount = 'berniesanders'
filenameMainTweet = directory + 'tweets_3-1.json'
filenameRetweet = directory + 'retweets' #Note need to append name
filenameFollowersID = directory + 'followersList.txt'
filenameFollowers = directory + 'followers.json'
filenameRelationships = directory + 'relationship.txt'

searchTerm = '#arkansasprimary'
filenameHashTag = 'trends/arkansasprimary.json'
# filenameState = 'trends/Arkansas.json'


# # Establish OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# print(json.dumps(api.rate_limit_status()))

# Store tweets in json file
def process_or_store(tweet, filename):
    with open(filename,'a') as f:
        f.write(json.dumps(tweet))
        f.write("\n")

## Step 1) Grab tweets from candidates on superTuesday and retweets
# for status in tweepy.Cursor(api.user_timeline,screen_name=twitterAccount,since_id=704639351565611008,max_id=704991282989379585).items():
#     process_or_store(status._json, filenameMainTweet)
#     print(json.dumps(status._json))

# # Read from file
# with open(filenameMainTweet, 'r') as f:
#     for line in f:
#         tweet = json.loads(line)
#         tweetID = json.dumps(tweet['id'])
#         print("id: " + tweetID)
#         for item in api.retweets(id=tweetID,count=100):
#             process_or_store(item._json,filenameRetweet+tweetID + '.json')



## Step 2), get follower ID and info of each candidate
def store_id_list(id, filename):
    with open(filename,'a') as f:
        print(id)
        f.write(str(id))
        f.write('\n')

# # Get ids of followers
# for follows in tweepy.Cursor(api.followers_ids,screen_name=twitterAccount).items():
#     store_id_list(follows,filenameFollowersID)

# Establish relationship between followers and popular social media
trumpID = 25073877
cruzID = 23022687
rubioID = 15745368
kasichID = 18020081
clintonID = 1339835893
sandersID = 216776631
cnnID = 759251
foxnewsID = 1367531
huffingtonpostID = 14511951
cnbcID = 20402945
nytimesID = 807095

# I am idiot for hardcoding this...
def storeRelationship(id, trumpFollow, cruzFollow, rubioFollow, kasichFollow, clintFollow, sandersFollow, cnnFollow, foxnewsFollow, huffingtonpostFollow, cnbcFollow, nytimesFollow,filename):
    with open(filename,'a') as f:
        f.write(str(id) + " " + str(trumpFollow)+ " " + str(cruzFollow)+ " " + str(rubioFollow)+ " " +
                str(kasichFollow)+ " " + str(clintFollow)+ " " + str(sandersFollow)+ " " + str(cnnFollow)+ " " +
                str(foxnewsFollow)+ " " + str(huffingtonpostFollow)+ " " + str(cnbcFollow)+ " " + str(nytimesFollow))
        f.write('\n')



########################################################################################################################
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Get info for each follower
totalIterations = 25

while 0 < 1:
    iteration1 = 0
    iteration2 = 0
    count = 0
    numLines = file_len(filenameFollowers)
    print(totalIterations)
    with open(filenameFollowersID, 'r') as f:
        for line in f:
            if count < numLines:
                #print("skipping")
                count = count + 1
            else:
                userID = int(line)
                print(userID)
                try:
                    user = api.get_user(id = userID)
                    process_or_store(user._json,filenameFollowers)
                except tweepy.TweepError:
                    print("catching")


                iteration1 = iteration1 + 1
                if(iteration1 == 180):
                    break


    # Determine relationship between each follower and other important political figures
    count = 0

    with open(filenameFollowersID, 'r') as f:
        for line in f:
            # userID = f.readline().replace("\n","")
            if count < numLines:
                #print("skipping")
                count = count + 1
            else:
                userID = line.replace("\n","")
                try:
                    trump = api.show_friendship(source_id=userID, target_id=trumpID)
                    cruz = api.show_friendship(source_id=userID, target_id=cruzID)
                    rubio = api.show_friendship(source_id=userID, target_id=rubioID)
                    kasich = api.show_friendship(source_id=userID, target_id=kasichID)
                    clinton = api.show_friendship(source_id=userID, target_id=clintonID)
                    sanders = api.show_friendship(source_id=userID, target_id=sandersID)
                    cnn = api.show_friendship(source_id=userID, target_id=cnnID)
                    foxnews = api.show_friendship(source_id=userID, target_id=foxnewsID)
                    huffingtonpost = api.show_friendship(source_id=userID, target_id=huffingtonpostID)
                    cnbc = api.show_friendship(source_id=userID, target_id=cnbcID)
                    nytimes = api.show_friendship(source_id=userID, target_id=nytimesID)
                    storeRelationship(userID,trump[0].following,cruz[0].following,rubio[0].following,kasich[0].following,
                              clinton[0].following,sanders[0].following,cnn[0].following,foxnews[0].following,
                              huffingtonpost[0].following,cnbc[0].following,nytimes[0].following,filenameRelationships)
                except tweepy.TweepError:
                    print("catching")
                iteration2 = iteration2 + 1
                if iteration2 == 16:
                    break
    totalIterations =  totalIterations + 1
    print('start sleep')

    if(totalIterations == 6):
        print('start cruz')
        directory = 'Cruz/'
        twitterAccount = 'tedcruz'
        filenameFollowersID = directory + 'followersList.txt'
        filenameFollowers = directory + 'followers.json'
        filenameRelationships = directory + 'relationship.txt'
    elif (totalIterations == 12):
        directory = 'Kasich/'
        twitterAccount = 'johnkasich'
        filenameFollowersID = directory + 'followersList.txt'
        filenameFollowers = directory + 'followers.json'
        filenameRelationships = directory + 'relationship.txt'
    elif (totalIterations == 18):
        directory = 'Rubio/'
        twitterAccount = 'marcorubio'
        filenameFollowersID = directory + 'followersList.txt'
        filenameFollowers = directory + 'followers.json'
        filenameRelationships = directory + 'relationship.txt'
    elif (totalIterations == 24):
        directory = 'Sanders/'
        twitterAccount = 'berniesanders'
        filenameFollowersID = directory + 'followersList.txt'
        filenameFollowers = directory + 'followers.json'
        filenameRelationships = directory + 'relationship.txt'

    time.sleep(905)



########################################################################################################################
# # 3) and 4) Search for tweets based on the hastag
# Note the 'since_id' is a random february 11th 2016 tweet to ensure tweets are from this year
# for search in tweepy.Cursor(api.search,q=searchTerm,since_id=697985393115836417).items():
#     process_or_store(search._json, filenameHashTag)



