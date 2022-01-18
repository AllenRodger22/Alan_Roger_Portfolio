from ast import Break
from bs4 import BeautifulSoup
import csv
import requests
response = requests.get('https://www.fundsexplorer.com.br/funds')

content = response.content

soup = BeautifulSoup(content,'lxml')

x = soup.find('div',attrs={'id':'fiis-list-container'})
list_fii=[]
while x != 'yufi11b':
    if x.string == 'YUFI11B':
        x = 'yufi11b'
        break
    x = x.find_next('div',attrs={'class':'col-md-3 col-xs-12'})
    x = x.find_next('span')
    print(x.string)
    list_fii.append(x.string.lower())


f = open('list_name_fii', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(['fii name'])
for i in range(346):
    writer.writerow([list_fii[i]])
f.close()