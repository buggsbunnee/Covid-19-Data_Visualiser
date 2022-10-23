import bs4
import requests
from matplotlib import pyplot as plt


res=requests.get('https://www.worldometers.info/coronavirus/')
soup=bs4.BeautifulSoup(res.text, "lxml")          #creating the beautiful soup object
elem=soup.select('tr')                            #selecting all the row elements in the main countries table from the site
countries=[]                                      #list to store the country names

cases=[]                                          #list to store the total cases for each country

for i in range(9,19):                             #looping over the elements to get the data for each country
    string=elem[i].text
    temp=string.split('\n')
    case=temp[3].replace(',','')
    case=int(case)
    countries.append(temp[2])
    cases.append(case)



cases.sort()                                      #plotting the number of cases v/s countries
countries.reverse()
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.bar(countries,cases)
plt.xlabel('Country')
plt.title('Top 10 Countries With Highest Number of CoronaVirus Cases')
plt.show()
