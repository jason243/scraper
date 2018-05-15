import os
import sys
import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import csv
import pandas as pd
import lxml

link = input('enter a ft fund data link: ') # grabs link
df_list = pd.read_html(link)
df_list[0].to_csv('test.csv')
