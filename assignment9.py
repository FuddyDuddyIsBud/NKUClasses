import requests
from bs4 import BeautifulSoup
import pandas as pd

#task1
url='https://www.marketwatch.com/investing/stock/aapl'

page=requests.get(url)

soup=beautifulSoup(page.txt,lxml)

print(soup)
#task2

soup.find('h2',{'class':'intraday__price'})
soup.find('div',{'class':'intraday__close'})

#task3

soup.find('div',{'class':'indicator indicator--yearly'})
soup.find('div',{'class':'range__header'})
soup.findall('div',{'class':'primary'})

#task3.2-4-5
url = 'https://www.nfl.com/standings/league/2019/reg/'
requests.get(url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

name = soup.find_all('thread','tr','td',class_='Division name')
wins = soup.find_all('thread','tr','td', class_='WINS')
losses = soup.find_all('thread', 'tr', 'td', class_='LOSSES')
ties = soup.find_all('thread', 'tr', 'td', class_='TIES')

name_list = [i.text for i in name]
wins_list=[i.text for i in wins]
losses_list = [i.text for i in losses]
ties_list = [i.text for i in ties]

table = pd.DataFrame({'name_list':'wins_list','losses_list':'ties_list'})
table = soup.find('table', class_ = 'd3-l-grid--outer d3-l-section-row nfl-o-standings')
headers=[i.txt.strip() for i in table.find_all('th')]
df=pd.DataFrame(columns=headers)

for j in table.findall('tr')[1:]:
    row_data=j.find_all('td')
    row = [tr.text for tr in row_data]
    length=len(df)
    df.loc[length]=row

df.to_csv('standingstable.csv')

