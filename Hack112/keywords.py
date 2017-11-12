import paralleldots

from paralleldots import set_api_key, get_api_key

set_api_key("97FJ7bd3rnhTmzIyYJiMY38ygPuUeZAbVdBSXPaJNZc")

from paralleldots import (similarity, ner, taxonomy, sentiment, keywords, 
intent, emotion, multilang, abuse)

def sortlist(l):
    vals = []
    out = []
    for elem in l:
        vals += [elem['confidence_score']]
    vals.sort()
    vals.reverse()
    for val in vals:
        for elem in l:
            if elem['confidence_score'] == val:
                out += [elem['keyword']]
    return out
    

def confidenceScores(text):
    dicto = keywords(text)
    list = dicto['keywords']
    out = sortlist(list)
    return out
    

    
    
    

#print(confidenceScores('''Mr Putin stood up to greet Mr Trump\nPresident Vladimir Putin feels insulted by allegations of Russian interference in the 2016 US election, Donald Trump has said after meeting him briefly at an Asia-Pacific summit in Vietnam.\n"He said he absolutely did not meddle in our election," the US leader said.\nMr Trump, who defeated Democratic rival Hillary Clinton, said the allegations were a "Democratic hit job".\nThe US intelligence community concluded earlier that Russia had indeed tried to sway the poll in favour of Mr Trump.\nThe US justice department has appointed special investigator Robert Mueller to examine any possible collusion involving Mr Trump's team, and legal action has already been taken against several former aides.\nWhat are the allegations against Russia?\nPresident Trump has refused to acknowledge a reported assessment by the CIA and other intelligence agencies that Russia was behind the hacking of the Democratic National Committee (DNC) in the run-up to last year's presidential election.\nThe contents of the emails, passed to Wikileaks and posted online, were embarrassing to the Democrats and shook up the presidential campaign, which ended in defeat for Hillary Clinton.\nIn addition to the Mueller inquiry, congressional committees have been set up to carry out their own investigations.\nRelations between the US and Russia have been strained for years, with the Kremlin long accusing Washington of seeking to sway elections in Russia and other ex-Soviet states including Ukraine and Georgia.\nWhile Russian hackers are widely suspected of involvement, there has been no conclusive link to the Kremlin.\nDenying that Russia had tried to interfere last year by fostering contacts with Mr Trump's campaign, Mr Putin told reporters in Vietnam: "Everything about the so-called Russian dossier in the US is a manifestation of a continuing domestic political struggle."\nWhat does Mr Trump say to the allegations?\nHe said he believed Mr Putin had been "very insulted by" the allegations and that was "not a good thing" for America.\n"He [Putin] said he didn't meddle," he added. "I asked him again."\nAsked if he believed Mr Putin, he replied, "He is very, very strong in the fact that he didn't do it. You have President Putin very strongly, vehemently says he has nothing to do with that. Now, you are not going to get into an argument, you are going to start talking about Syria and the Ukraine."\nTrump out on a limb again\nAleem Maqbool, BBC News, Da Nang\nDonald Trump once again goes against the findings of his own intelligence agencies.\nBecause although the US justice department is investigating the scale and nature of Russian interference in the election of 2016 (and any links to the Trump campaign), the American intelligence community has already long determined that Russia did, indeed, interfere.\nYet Mr Trump suggested this story was not only entirely fabricated by his political opponents, it might even be costing lives in Syria, because it is getting in the way of his relationship with the Russian president and hampering their ability to help solve the conflict together.\n"People will die because of it, and it's a pure hit job, and it's artificially induced and that's a shame," he said.\nIt is hard to know what the president hopes to achieve with this type of rhetoric. The investigation goes on.\nHow did the two presidents get on in Vietnam?\nMr Trump and Mr Putin met for the first time in July at a G20 summit in the German city of Hamburg. In Da Nang they were seen chatting briefly on three occasions within 24 hours during the Asia-Pacific Economic Co-operation (Apec) summit.\nHowever, they had no formal bilateral meeting, with Mr Putin blaming it on scheduling and protocol.\nThey had warm words for each other, with the US president talking of their mutual "very good feeling" and the Russian leader describing his counterpart as "well-mannered... and comfortable to deal with".\nThey did manage to sign off a statement vowing to continue the battle against so-called Islamic State in Syria until the militants are defeated and calling for a political solution to the conflict.\nHow far has US justice department investigation progressed?\nLast month, former Trump campaign adviser George Papadopoulos pleaded guilty to having lied to the Federal Bureau of Investigation (FBI) about the timing of meetings with alleged go-betweens for Russia.\nHe testified that Russian nationals had contacted him in an attempt to gain influence with the Trump campaign, offering "dirt" in the form of "thousands of emails" on Mrs Clinton in April 2016 - two months before the DNC emails were leaked.\nMr Trump has played down the importance of Mr Papadopoulos, calling him a "low-level volunteer" and "liar".\nOn Saturday, Mr Putin brushed aside US media reports that a woman wrongly identified by Mr Papadopoulos as the Russian president's niece had offered to help broker meetings with Kremlin officials.\n"I do not know anything about it and I think it is just some fantasies," Mr Putin said.\nMr Trump's former campaign manager, Paul Manafort, and an associate were also placed under house arrest on charges of money laundering as a result of the Mueller inquiry, but the charges do not relate to the election.'''))