import os
import sys
import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import csv

# test link:  https://markets.ft.com/data/funds/tearsheet/historical?s=GB00BHZK8872:GBX


link = input('enter a ft fund data link: ') # grabs link
a = requests.get(link) # saves page
myfile = a.text # converts page to text file
b = BeautifulSoup(myfile, 'html.parser') # parses html

c = b.find('section' , attrs = {'class' : 'mod-main-content'} ) # finds date
# d = b.find('td', attrs={'class': ''} ) # finds corresponding closing price
spreadsheet = c.text.strip()
# cprice = d.text.strip() # strip() is used to remove starting and trailing

print(spreadsheet)
# print(cprice)

with open('index.csv' , 'w' , newline = '' ) as csv_file:
    writer = csv.writer(csv_file , lineterminator = '----' )
    writer.writerow([spreadsheet])

# print(myfile)
# b = open("test.txt", myfile)
