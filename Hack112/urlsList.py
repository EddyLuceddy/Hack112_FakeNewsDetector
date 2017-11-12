from googlemaster.google import search
from keywords import confidenceScores

def getUrlList(keywords,origURL):
    urlList = []
    
    for url in search('%s'%(" ".join(keywords)), stop=20):
        if url != origURL and len(urlList) < 5:
            urlList.append(url)

    return urlList

#print(getUrlList(['argument', 'statement', 'investigation', 'Russian interference', 'Trump President Vladimir', 'two presidents', 'three occasions within hours', 'manage', 'comfortable', 'fact', 'allegations', 'Vietnam Mr Trump', 'Da Nang', 'Mr Putin stood', 'nothing', 'AsiaPacific', 'strongly', 'briefly', 'strong', 'Mr Putin', 'Putin', 'Syria', 'Cooperation Apec', 'battle', 'deal'], ""))