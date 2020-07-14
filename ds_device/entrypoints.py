import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from scraper import displaySearch
from gui import mainApp


def searchDataset():
    keyword = 'covid'
    ds = displaySearch(keyword) #Initiate search class 
    results = ds.retrieveLinks() 
    for i in results: 
        print(i)


if __name__ == '__main__':
    print('Commencing Search')
    searchDataset()
    print('Search Complete')
    #mainApp()


