import newspaper
import requests
from bs4 import BeautifulSoup

def getTextFromURL(url):
    a = newspaper.Article(url, language = 'en')
    a.download()
    a.parse()
    return a.text

def getTitleFromURL(url):
    a = newspaper.Article(url, language = 'en')
    a.download()
    a.parse()
    return a.title