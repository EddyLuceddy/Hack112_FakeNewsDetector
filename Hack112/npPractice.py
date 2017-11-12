import newspaper
import requests
from bs4 import BeautifulSoup

def getTextFromURL():
    url = 'http://www.bbc.com/news/world-us-canada-41954436'
    a = newspaper.Article(url, language='en')
    a.download()
    a.parse()
    print(a.text)
    
def getLinksFromURLs():
    urls = [('http://feeds.bbci.co.uk/news/rss.xml?edition=us', 'bbc'), ( 'http://rss.cnn.com/rss/cnn_topstories.rss', 'cnn')]
    L = []
    for url in urls:
        L += getAllLinks(*url)
    return L
    
def getAllLinks(url, web):
    website = requests.get(url)
    source = website.text
    parser = BeautifulSoup(source,'html.parser')
    links = []
    for link in parser.find_all("guid"):
        lnk = str(link)
        if web in lnk:
            links.append(removeHTML(link))
    return links
        
def removeHTML(text):
    HTML = False
    newText = []
    for c in text:
        if c in ['>', '<']:
            HTML = not HTML
        else:
            newText.append(c)
    return ''.join(newText)
    
getTextFromURL()