import os
import sys
import requests
from bs4 import BeautifulSoup 

link = "https://markets.ft.com/data/funds/tearsheet/historical?s=GB00BHZK8872:GBX" # grabs link
a = requests.get(link) # saves page
myfile = a.text # converts page to text file
b = BeautifulSoup(myfile, 'html.parser') # parses html

c = b.find('td', attrs={'class': 'mod-ui-table__cell--text'} ) # finds date
d = b.find('td', attrs={'class': ''} ) # finds corresponding closing price
date = c.text.strip()
cprice = d.text.strip() # strip() is used to remove starting and trailing

print(date)
print(cprice)

# print(myfile)
# b = open("test.txt", myfile)
