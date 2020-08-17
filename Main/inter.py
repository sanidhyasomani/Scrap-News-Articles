
import urllib.request
from bs4 import BeautifulSoup
from Content import content
from datetime import date

def check(year):
    check = year >= 2010 and year <= 2019
    if check == False:
        print("Enter year between 2010 and 2019")
        year = int(input())
        check(year)
        
year = int(input())
check(year)

for y in range(0,12):
    if y!=11:
        i = (date(year, y+2, 1) - date(year, y+1, 1)).days
        i = i - 1
    else: 
        i = 30
    for z in range(0,i):
        fill = 40179 + (date(year, y+1, z+1) - date(2010, 1, 1)).days
        url = "https://timesofindia.indiatimes.com/" + str(year) + "/" + str(y+1) + "/" + str(z + 1) + "/archivelist/year-2010,month-1,starttime-" + str(fill)  + ".cms"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page)
        divs = soup.find_all('table', {"class" : "cnt"})

        for div in divs:
            links = div.find_all("a")

        text = [] 
        l = []
        
        i = 0
        for lin in links:
            l.append([])
            l[i] = lin.get("href")
            text.append([])
            text[i] = lin.text
            i = i + 1
            
            text1 = []
            l1 = []
            
        for i in range(3,len(text)-21):
            text1.append([])
            text1[i-3] = text[i]
            l1.append([])
            l1[i-3] = l[i]
                
        if z == 0:
            j = 0
            headings = []
            final_links = []
                    
                    
        term = "HIV"
        for i in range(len(text1)):
            words = text1[i].split()
            if term in words:
                headings.append([])
                headings[j] = text1[i]
                final_links.append([])
                final_links[j] = l1[i]
                j = j + 1
    print(headings)
    content(final_links, headings, y, year)


