#! python3
# queries a term on merriam-webster.com and returns the thesarus entries
# need /home/<name>/code folder if you want to save to a text file. or just comment those lines out
# if necessary: pip install beautifulsoup4; pip install requests

import requests, sys, webbrowser, bs4, os.path, re

queryTerm = input('Enter search term (ex: district): ')

print(queryTerm)

#res = requests.get('http://google.com/search?q=synonym+' + queryTerm)
res = requests.get('https://www.merriam-webster.com/thesaurus/' + queryTerm)
res.raise_for_status()

# return results as text
soup = bs4.BeautifulSoup(res.text, "html.parser")
#print(soup)
# select results
linkElems = soup.find_all("div", class_="thes-list-content")
#linkElems = soup.select("div > a")
#print(linkElems)
#print(linkElems[1])
#print(len(linkElems))

s = str(linkElems[1])
bracketRemove = re.sub('<[^>]+>', '', s)
line = bracketRemove.replace('\n',',')
line = line.replace(',,',',')
#print(line)
SynList = [x.strip() for x in line.split(',')]

Intonation = "What is my "
for i in SynList:
    print('"'+Intonation + str(i) +'",')
    print('"' + "What " + str(i) + " am I in" + '",'+ '\n')

print("starting google search")
#as a function ... won't work. div classes will always be different for websites
res = requests.get('http://google.com/search?q=synonym+' + queryTerm)
res.raise_for_status()

# return results as text
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup)
# select results
linkElems = soup.find_all("span", class_="SDZsVb")
#linkElems = soup.select("div > a")
print(linkElems)
#print(linkElems[1])
#print(len(linkElems))

s = str(linkElems[1])
bracketRemove = re.sub('<[^>]+>', '', s)
line = bracketRemove.replace('\n',',')
line = line.replace(',,',',')
#print(line)
SynList = [x.strip() for x in line.split(',')]

Intonation = "What is my "
for i in SynList:
    print('"'+Intonation + str(i) +'",')
    print('"' + "What " + str(i) + " am I in" + '",'+ '\n')