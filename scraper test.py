import os
import sys
import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import csv

link = "https://markets.ft.com/data/funds/tearsheet/historical?s=GB00BHZK8872:GBX" # grabs link
a = requests.get(link) # saves page
myfile = a.text # converts page to text file
b = BeautifulSoup(myfile, 'html.parser') # parses html

c = b.find('div' , attrs = {'class' : 'mod-ui-table--freeze-pane__container'} ) # finds date
# d = b.find('td', attrs={'class': ''} ) # finds corresponding closing price
spreadsheet = c.text.strip()
sort = csv.reader(spreadsheet, delimiter = '-')
# cprice = d.text.strip() # strip() is used to remove starting and trailing

print(sort)
# print(cprice)

with open('index.csv' , 'w' , newline = '' ) as csv_file:
    writer = csv.writer(csv_file )
    writer.writerow([sort])

# print(myfile)
# b = open("test.txt", myfile)
