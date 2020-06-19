#%% Import libraries 
import pandas as pd 
import time 
import urllib.request
import requests
import re
import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class displaySearch():
    '''Display csv datasets from listed websites based on the search term''' 

    def __init__(self,keyword):
        self.browser = browserStart()
        kgl_info = __kaggleSearch(term = keyword)
        aws_info = __awsSearch(term = keyword)
        for links in kgl_info:
            print(links)
        for links in aws_info:
            print(links)

    @staticmethod
    def browserStart():
        '''Start Firefox browser in headless mode'''
        opts = Options()
        opts.headless = True
        browser = Firefox(options=opts)
        return browser

    def __kaggleSearch(term = None, browser = self.browser): 
        '''Search for csv datasets on Kaggle and return a list of hyperlinks'''
        kgl_links = []
        kgl_xpath = '//ul/li/a'
        kgl_url = 'https://www.kaggle.com/datasets?search='+str(term)
        browser.get(kgl_url)
        kgl_elems = browser.find_elements_by_xpath(kgl_xpath)
        for elems in kgl_elems:
            kgl_links.append(elems.get_attribute('href'))
        return kgl_links

    def __awsSearch(term = None, browser = self.browser): 
        '''Search for csv datasets on AWS and return a list of hyperlinks'''
        aws_links = []
        aws_url = 'https://registry.opendata.aws/'
        browser.get(aws_url)
        browser.find_element_by_xpath('//*[@id="search-box"]').send_keys(term)
        aws_xpath = '//div[contains(@class,"dataset") and not(@style="display:none;")]/*/a'
        aws_elems = browser.find_elements_by_xpath(xpath_aws)
        for elems in aws_links:
            if elems.text != '': #the site hides links which is not relevant to the search 
                aws_links.append(links.get_attribute('href')) 
        return aws_links

