import pandas as pd 
import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from scraper import displaySearch



def searchDataset():
    keyword = 'covid'
    displaySearch(keyword) #Initiate search class 

if __name__ == '__main__':
    print('Commencing Search')
    searchDataset()



