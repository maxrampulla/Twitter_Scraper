import csv
import nltk
import matplotlib.pyplot as plt
import numpy as np

#reads the csv into a list
words = []
numberOfWords = 0
with open('listfile.csv', 'r') as file:
    for row in file:
        words.append(row)
        numberOfWords += 1
words = [i[:(len(i)-1)] for i in words] # removes /n from words

#filters out additional words that do not add value and muddle data
filter = ["http","rt","like","wa","amp","one","let","also","many","said","back","ha","really",]
filteredWords = [i for i in words if i not in filter]

#frequency of csv words
from nltk.probability import FreqDist
fdist = FreqDist(filteredWords)
most = fdist.most_common(50)
print(most)

#theme distriubtion
politics = ["trump", "american", "black" "world", "pandemic", "mask", "florida", "republican", "biden", "police", "election"]
politicsCount = 0
tech = ["founder", "company", "startup", "business", "online", "tech", "investory", "stock", "launch"]
techCount = 0
other = 0
total = 0


for i in most:
    if i[0] in politics:
        politicsCount += i[1]
        total += i[1]
    elif i[0] in tech:
        techCount += i[1]
        total += i[1]
    else:
        other += i[1]
        total += i[1]

#creates a pie chart of distrubtion
plt.pie([politicsCount, techCount])
plt.legend(["Politics & Current Events", "Tech Industry & Business"], loc=4)
plt.title("Community Distribution Twitter")
plt.show()

values = []
keys = []
for i in most:
    values.append(i[1])
    keys.append(i[0])

#creates a graph
plt.bar(range(len(most)), values, align='center')
plt.xticks(range(len(most)), keys, rotation = 90)
plt.title("Twitter Feed Word Frequency Distribution")
plt.xlabel("Unique Word Occurence")
plt.ylabel("Frequency of Word Use out of %s Words Analyzed" %numberOfWords)


plt.show()
