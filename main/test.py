import tweepy

# authenticaiton for twitter developer
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)

#returns friends list and parses descriptions in flowwing bio
data = {}
data["friends"] = []
for friend in tweepy.Cursor(api.friends, "@MaxRampulla").items(300):
    data["friends"].append({
    "description" : friend.description,
    "location" : friend.location
    })

#word tokenization for all text of tweets:
from nltk.tokenize import word_tokenize
text ="" #string that holds all text

for i in data["friends"]:
    text = text + " " + i["description"]

token = word_tokenize(text) #tokenizes bodies of tweets

#turns all works into lowercase
lowerToken = [i.lower() for i in token]

#filters out non-alphanumeric
filToken = [i for i in lowerToken if i.isalnum()]

#lemmatizaton
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemToken = [lemmatizer.lemmatize(i) for i in filToken]

#stop words for english filtered out of text
from nltk.corpus import stopwords
a = set(stopwords.words("english"))

finalToken = [x for x in lemToken if x not in a]

#saves list externally
with open('listfilebios.csv', 'a') as file:
    for i in finalToken:
        file.write('%s\n' % i)


#records the frequency of words
from nltk.probability import FreqDist
fdist = FreqDist(finalToken)

print(fdist.pprint(500))
