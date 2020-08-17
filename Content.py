
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def content(link, text, m, year):
    for i in range(len(link)):
        l = link[i].split(":")
        link[i] = l[0] + 's:' + l[1]
    content1 = []
    for i in range(len(link)):
        try:
            page = urllib.request.urlopen(link[i])
            soup = BeautifulSoup(page)
            divs = soup.find_all('div', {"class" : "Normal"})
            if divs!=[]:
                for div in divs:
                    content1.append([])
                    content1[i] = div.text
            else:
                content1.append([])
                content1[i] = "No article on the website!"
        except:
            content1.append([])
            content1[i] = "HTTPError404: URL either moved or removed by the agency"    

            
    name = str(year) + "_" + str(m) + ".xlsx"
    if(len(content1)!=len(link)):
        d = len(content1) - len(link)
        content1 = content1[:-d or None]
    Final_Table = pd.DataFrame(np.column_stack([text, content1, link]), columns = ['Headline','Content','URL'])
    Final_Table.to_excel(name)
