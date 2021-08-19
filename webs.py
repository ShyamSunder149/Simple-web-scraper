import requests
from bs4 import BeautifulSoup

URL='https://coinmarketcap.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content,features='lxml')
resultsprice = soup.find_all(class_='sc-131di3y-0 cLgOOr')
resultsname = soup.find_all(class_='sc-1eb5slv-0 iJjGCS')

resultsname2 =[]
resultsprice2 =[]

for i in range(len(resultsprice)):
	resultsprice2.append(resultsprice[i].text)
for i in range(8,len(resultsname)):
	resultsname2.append(resultsname[i].text)

for i,j in zip(resultsname2,resultsprice2):
	print(i+"->"+j)