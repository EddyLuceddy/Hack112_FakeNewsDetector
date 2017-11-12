from urlsList import getUrlList
from keywords import confidenceScores
from sentiments import sentiment_text
from urlToText import getTextFromURL
from classify import classify
import time

def main(text,origURL):
    sentimentScoreList = []
    confidenceScoreList =[]
    keywords = confidenceScores(text)
    #print(keywords)
    
    urlList = getUrlList(keywords, origURL)
    print(urlList)
    #print(len(urlList))
    newsConfidence = classify(text)
    #print(newsConfidence)
    endWebsite = origURL.find(".com")
    origURLMain = origURL[:endWebsite]
    for url in urlList:
        #print(sentimentScoreList)
        try:
            newText = getTextFromURL(url)
        except:
            continue
        #print(newText)
        if len(newText) == 0 or url[:endWebsite] == origURLMain:
            continue
        sentimentScoreList.append(sentiment_text(newText))
        try:
            currentConfidence = classify(newText)
        except:
            continue
        if currentConfidence == None:
            confidenceScoreList.append(0)
        else:
            confidenceScoreList.append(currentConfidence)
    textSentimentScore = sentiment_text(text)
    numberOfSources = len(sentimentScoreList)
    #print(numOfSources, textSentimentScore, sentimentScoreList)
    return numberOfSources, newsConfidence, textSentimentScore, confidenceScoreList, \
    sentimentScoreList

urlLink = "http://www.bbc.com/news/entertainment-arts-41955113"
sampleText = getTextFromURL(urlLink)
scores = main(sampleText, urlLink)
#realLink = "http://www.bbc.com/news/entertainment-arts-41955113"
#main of text from realLink is (4, 0.6899999976158142, -0.30000001192092896, [0.6499999761581421, 0.5799999833106995, 0.6100000143051147], [-0.30000001192092896, 0.20000000298023224, -0.20000000298023224, -0.30000001192092896])
#score of this is 76.14356055982385
#fakeLink = https://www.theonion.com/toddler-scientists-finally-determine-number-of-peas-tha-1820347088
#main of text from fakeLink is (4, None, -0.30000001192092896, [0, 0, 0], [-0.30000001192092896, 0.8999999761581421, 0.10000000149011612, 0.0])
#score of this is 45.32588031453411
#print(scores)

def getFakeNewsMeter(scores):
    noOfSources = scores[0]
    confidence, sentiment = scores[1], scores[2]
    othersConfidence, othersSentiment = average(scores[3]), ( 1 - variance(scores[4]))
    if confidence == None: confidence = 0
    e = 1
    a = 1
    b = 1
    c = 1
    d = 1
    sourcesScore = e * (noOfSources/5)
    ownSentimentAndConfidence = a * (1 - sentiment**2) + b * confidence
    othersSentiment =  c * othersSentiment
    othersConfidence = d * othersConfidence
    return (sourcesScore + ownSentimentAndConfidence + othersSentiment + othersConfidence) \
    /(a+b+c+d+e) * 100

def average(L):
    if len(L) == 0:
        return None
    else:
        return sum(L)/len(L)

def variance(L):
    return (average([i**2 for i in L]) - average(L)**2)**0.5

#print(getFakeNewsMeter(scores))
#print(sampleText)
#classify(sampleText)

#for url in urls:
#    sampleText = getTextFromURL(url)
#    print("The text is", sampleText)
#    sentiment_text(sampleText)