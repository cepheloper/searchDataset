import pandas as pd 
import time 
import urllib.request
import requests
import re
import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import sys
from scraper import displaySearch



def searchDataset():
    keyword = 'covid'
    dsr = displaySearch() #Initiate search class 
    dsr.main(keyword)

if __name__ == '__main__':
    print('Commencing Search')
    searchDataset()



