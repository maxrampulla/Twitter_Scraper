import json
import tweepy
import numpy as np
import nltk
import os
import nltk.corpus
import csv
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# sets authentication handlers
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)

# creates a dictionary of 500 tweets that are found on my timeline when the
# program is run
data = {}
data["tweets"] = []

number = 0

public_tweets = api.home_timeline(count=500)
for tweet in public_tweets:
    data["tweets"].append({
        "id": tweet.id,
        "userName": tweet.user.name,
        "text": tweet.text,
        "user": tweet.user.id,
        "hashtags": tweet.entities["hashtags"]
    })
    number += 1

#word tokenization for all text of tweets:
text = ""  # string that holds all text

for i in data["tweets"]:
    text = text + " " + i["text"]

token = word_tokenize(text) #tokenizes bodies of tweets

#turns all works into lowercase
lowerToken = [i.lower() for i in token]

#filters out non-alphanumeric
filToken = [i for i in lowerToken if i.isalnum()]

#lemmatizaton
lemmatizer = WordNetLemmatizer()
lemToken = [lemmatizer.lemmatize(i) for i in filToken]

#stop words for english filtered out of text
a = set(stopwords.words("english"))

finalToken = [x for x in lemToken if x not in a]

#saves list externally
with open('listfile.csv', 'a') as file:
    for i in finalToken:
        file.write('%s\n' % i)


#records the frequency of words
fdist = FreqDist(finalToken)

print(fdist.pprint(500))
print(number)
