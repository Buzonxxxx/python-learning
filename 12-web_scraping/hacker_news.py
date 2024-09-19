import requests
from bs4 import BeautifulSoup
import pprint

# CSS Selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda item: item['votes'], reverse=True)
    

def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)

        if i < len(subtext):
            vote = subtext[i].select('.score')
            if vote:
                point = int(vote[0].get_text().replace(' points', '')) 
                if point >= 100:
                    hn.append({'title': title, 'link': href, 'votes': point})
    
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))