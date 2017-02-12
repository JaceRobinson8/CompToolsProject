# Jace Robinson
# 3-6-16
# CS 3250 Dataminer of twitter

import json
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import operator
from collections import Counter
import os


####set files to convert
directory = "Clinton/"
candidate = 'clinton'

#tweets
with open('tweets/tweets' + candidate + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # writer.writerow(['text', 'id', 'created_at', 'favorite_count', 'retweet_count', 'place', 'geo', 'coordinates',
    #                  'candidate'])
    with open(directory + 'tweets_3-1.json', 'r') as f:
        for line in f:
            print("******************")
            # line = f.readline()
            tweet = json.loads(line) # load it as Python dict
            print(tweet['text'].replace(",",""))
            print(tweet['id'])
            print(tweet['created_at'])
            print(tweet['favorite_count'])
            print(tweet['retweet_count'])
            print(tweet['place'])
            print(tweet['geo'])
            print(tweet['coordinates'])
            # print(tweet['location'])
            # print("::::::::::")
            # print(tweet['user']['id'])
            # print(tweet['user']['followers_count'])
            # print(tweet['user']['location'])
            # print(tweet['user']['name'])
            # print(tweet['user']['friends_count'])
            # print(tweet['user']['favourites_count'])
            # print(tweet['user']['screen_name'])
            # print(tweet['user']['created_at'])
            # print(tweet['user']['description'])
            # print(tweet['user']['statuses_count'])
            # print(tweet['user']['time_zone'])
            # print(null)
            # print(json.dumps(tweet, indent=4)) # pretty-print
            try:
                writer.writerow([str(tweet['text'].replace(",","")) , str(tweet['id']) , str(tweet['created_at']) ,
                            str(tweet['favorite_count']) , str(tweet['retweet_count']) , str(tweet['place']) , str(tweet['geo']) ,
                            str(tweet['coordinates']) , candidate])
            except UnicodeEncodeError:
                print("skipping, error")


#retweets
# with open('retweets' + candidate + '.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(['text', 'id', 'created_at', 'favorite_count', 'retweet_count', 'place', 'geo', 'coordinates',
#                      'uid', 'ufollowers_count', 'ulocation', 'uname', 'ufriends_count', 'ufavourites_count',
#                      'uscreen_name', 'ucreated_at', 'udescription', 'ustatuses_count', 'utime_zone', 'candidate'])
#     for path, subdirs, files in os.walk(r'/home/jace/CompTools/project midterm/' + directory):
#         for filename1 in files:
#             if str(filename1).find("retweets") == 0:
#                 print(str(filename1))
#                 with open(directory + filename1, 'r') as f:
#                     for line in f:
#                         print("******************")
#                         # line = f.readline()
#                         tweet = json.loads(line) # load it as Python dict
#                         print(tweet['text'].replace(",",""))
#                         print(tweet['id'])
#                         print(tweet['created_at'])
#                         print(tweet['favorite_count'])
#                         print(tweet['retweet_count'])
#                         print(tweet['place'])
#                         print(tweet['geo'])
#                         print(tweet['coordinates'])
#                         # print(tweet['location'])
#                         print("::::::::::")
#                         print(tweet['user']['id'])
#                         print(tweet['user']['followers_count'])
#                         print(tweet['user']['location'])
#                         print(tweet['user']['name'])
#                         print(tweet['user']['friends_count'])
#                         print(tweet['user']['favourites_count'])
#                         print(tweet['user']['screen_name'])
#                         print(tweet['user']['created_at'])
#                         print(tweet['user']['description'])
#                         print(tweet['user']['statuses_count'])
#                         print(tweet['user']['time_zone'])
#                         # print(null)
#                         # print(json.dumps(tweet, indent=4)) # pretty-print
#                         try:
#                             writer.writerow([str(tweet['text'].replace(",","")) , str(tweet['id']) , str(tweet['created_at']) ,
#                                         str(tweet['favorite_count']) , str(tweet['retweet_count']) , str(tweet['place']) , str(tweet['geo']) ,
#                                         str(tweet['coordinates']) , str(tweet['user']['id']) , str(tweet['user']['followers_count']) , str(tweet['user']['location'].replace(",","")),
#                                         str(tweet['user']['name'].replace(",","")) , str(tweet['user']['friends_count']) , str(tweet['user']['favourites_count']) ,
#                                         str(tweet['user']['screen_name'].replace(",","")) , str(tweet['user']['created_at']) ,
#                                         str(tweet['user']['description'].replace(",","")) , str(tweet['user']['statuses_count']) , str(tweet['user']['time_zone']),candidate])
#                         except UnicodeEncodeError:
#                             print("skipping, error")


#followers
# with open('followers/followers' + candidate +'.csv', 'wb') as csvfile:
#     with open(directory + "followers.json", 'r') as f:
#         writer = csv.writer(csvfile, delimiter=',')
#         # writer.writerow(['uid','ufollowers_count','ulocation','uname','ufriends_count','ufavourites_count',
#         #                  'uscreen_name','ucreated_at','udescription','ustatuses_count','utime_zone', 'candidate'])
#         for line in f:
#             print("******************")
#             # line = f.readline()
#             tweet = json.loads(line) # load it as Python dict
#             print(tweet['id'])
#             print(tweet['followers_count'])
#             print(tweet['location'])
#             print(tweet['name'])
#             print(tweet['friends_count'])
#             print(tweet['favourites_count'])
#             print(tweet['screen_name'])
#             print(tweet['created_at'])
#             print(tweet['description'])
#             print(tweet['statuses_count'])
#             print(tweet['time_zone'])
#             # print(null)
#             # print(json.dumps(tweet, indent=4)) # pretty-print
#             try:
#                 writer.writerow([str(tweet['id']) , str(tweet['followers_count']) , str(tweet['location'].replace(",","")),
#                             str(tweet['name'].replace(",","")) , str(tweet['friends_count']) , str(tweet['favourites_count']) ,
#                             str(tweet['screen_name'].replace(",","")) , str(tweet['created_at']) ,
#                             str(tweet['description'].replace(",","")) , str(tweet['statuses_count']) , str(tweet['time_zone']),candidate])
#             except UnicodeEncodeError:
#                 print("skipping, error")

#followers connections
# with open(directory + 'relationship.txt') as fin, open('followers/relationship' + candidate + '.csv', 'w') as fout:
#     o=csv.writer(fout)
#     o.writerow(['id', 'trump','cruz','rubio','kasich','clinton','sanders','cnn','foxnews','huffingtonpost','cnbc','nytimes','candidate'])
#     for line in fin:
#         line = line + ' ' + candidate
#         o.writerow(line.split())

#superTuesday Tweets



#relationship



# #trends
# with open('trendsFinal/trends.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(['text', 'id', 'created_at', 'favorite_count', 'retweet_count', 'place', 'geo', 'coordinates',
#                      'uid', 'ufollowers_count', 'ulocation', 'uname', 'ufriends_count', 'ufavourites_count',
#                      'uscreen_name', 'ucreated_at', 'udescription', 'ustatuses_count', 'utime_zone', 'subject'])
#     for path, subdirs, files in os.walk(r'/home/jace/CompTools/project midterm/' + directory):
#         for filename1 in files:
#             subject = str(filename1).replace(".json","")
#             with open(directory + str(filename1), 'r') as f:
#                 for line in f:
#                     print("******************")
#                     # line = f.readline()
#                     tweet = json.loads(line) # load it as Python dict
#                     print(tweet['text'].replace(",",""))
#                     print(tweet['id'])
#                     print(tweet['created_at'])
#                     print(tweet['favorite_count'])
#                     print(tweet['retweet_count'])
#                     print(tweet['place'])
#                     print(tweet['geo'])
#                     print(tweet['coordinates'])
#                     # print(tweet['location'])
#                     print("::::::::::")
#                     print(tweet['user']['id'])
#                     print(tweet['user']['followers_count'])
#                     print(tweet['user']['location'])
#                     print(tweet['user']['name'])
#                     print(tweet['user']['friends_count'])
#                     print(tweet['user']['favourites_count'])
#                     print(tweet['user']['screen_name'])
#                     print(tweet['user']['created_at'])
#                     print(tweet['user']['description'])
#                     print(tweet['user']['statuses_count'])
#                     print(tweet['user']['time_zone'])
#                     # print(null)
#                     # print(json.dumps(tweet, indent=4)) # pretty-print
#                     try:
#                         writer.writerow([str(tweet['text'].replace(",","")) , str(tweet['id']) , str(tweet['created_at']) ,
#                                     str(tweet['favorite_count']) , str(tweet['retweet_count']) , str(tweet['place']) , str(tweet['geo']) ,
#                                     str(tweet['coordinates']) , str(tweet['user']['id']) , str(tweet['user']['followers_count']) , str(tweet['user']['location'].replace(",","")),
#                                     str(tweet['user']['name'].replace(",","")) , str(tweet['user']['friends_count']) , str(tweet['user']['favourites_count']) ,
#                                     str(tweet['user']['screen_name'].replace(",","")) , str(tweet['user']['created_at']) ,
#                                     str(tweet['user']['description'].replace(",","")) , str(tweet['user']['statuses_count']) , str(tweet['user']['time_zone']),subject])
#                     except UnicodeEncodeError:
#                         print("skipping, error")

# # Now convert a trends.csv file into WC (word cloud) file where each row is a word
# def preprocess(text):
#     return word_tokenize(text.lower())
#
#
# punctuation = list(string.punctuation)
# stop = stopwords.words('english') + punctuation + ['rt', 'via','https','http', '\'s', "\'\'", "\"", '``','...']
#
# fileName10 = 'tedcruz'
# numWords = 50
#
# fname = 'trends/' + fileName10 + '.json'
# with open(fname, 'r') as f:
#     count_all = Counter()
#     for line in f:
#         tweet = json.loads(line)
#         # Create a list with all the terms
#         terms_all = [term for term in preprocess(tweet['text']) if term not in stop]
#         # Update the counter
#         count_all.update(terms_all)
#     # Print the first 5 most frequent words
#     with open('trendsFinal/wc' + fileName10 + '.csv', 'wb') as csvfile:
#         writer = csv.writer(csvfile, delimiter=',')
#         writer.writerow(['word','count'])
#         for k,v in count_all.most_common(numWords):
#             try:
#                 writer.writerow([str(k), str(v)])
#             except UnicodeEncodeError:
#                 print("skipping, error")






