#%% Import libraries 
import pandas as pd 
import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class displaySearch():
    '''Display csv datasets from listed websites based on the search term''' 

    def __init__(self, keyword):
        self.logger = self.initLogger()
        self.keyword = keyword
        self.browser = self.browserStart()
        try:
            kgl_info = self.__kaggleSearch(term = self.keyword)
            aws_info = self.__awsSearch(term = self.keyword)
            for links in kgl_info:
                print(links)
            for links in aws_info:
                print(links)
        except Exception:
            logger.exception("Error in displaySearch")

    @staticmethod
    def initLogger():
        '''Initiate the log to record activity from info level'''
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # define file handler and set formatter
        file_handler = logging.FileHandler('ds_device.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')      
        file_handler.setFormatter(formatter)  
        logger.addHandler(file_handler) # add file handler to logger
        return logger

    @staticmethod
    def browserStart():
        '''Start Firefox browser in headless mode'''
        opts = Options()
        opts.headless = True
        browser = Firefox(options=opts)
        return browser

    def __kaggleSearch(self, term = None, browser = None ): 
        '''Search for csv datasets on Kaggle and return a list of hyperlinks'''
        if not browser:
            browser = self.browser
        kgl_links = []
        kgl_xpath = '//ul/li/a'
        kgl_url = 'https://www.kaggle.com/datasets?search='+str(term)
        browser.get(kgl_url)
        kgl_elems = browser.find_elements_by_xpath(kgl_xpath)
        for elems in kgl_elems:
            kgl_links.append(elems.get_attribute('href'))
        return kgl_links

    def __awsSearch(self, term = None, browser = None): 
        '''Search for csv datasets on AWS and return a list of hyperlinks'''
        if not browser:
            browser = self.browser
        aws_links = []
        aws_url = 'https://registry.opendata.aws/'
        browser.get(aws_url)
        browser.find_element_by_xpath('//*[@id="search-box"]').send_keys(term)
        aws_xpath = '//div[contains(@class,"dataset") and not(@style="display:none;")]/*/a'
        aws_elems = browser.find_elements_by_xpath(aws_xpath)
        for elems in aws_elems:
            if elems.text != '': #the site hides links which is not relevant to the search 
                aws_links.append(elems.get_attribute('href')) 
        return aws_links


    
