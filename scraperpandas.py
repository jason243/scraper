import os
import sys
import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import csv
import pandas as pd
import lxml


ISINlist = []
while True:
    print('enter an ISIN or nothing to stop: ')
    ISIN = input()
    link = 'https://markets.ft.com/data/funds/tearsheet/historical?s=' + ISIN
    df_list = pd.read_html(link)
    df_list[0].to_csv('test.csv')
    if link == '':
        break
    ISINlist = ISINlist + [ISIN]
print('The cat names are:')
for ISIN in ISINlist:
    print(' ' + ISIN)
