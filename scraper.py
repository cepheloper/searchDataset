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

#%% Set Browser 
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser = Firefox()

#%% Set URL
search_term = 'baseball'
url = 'https://www.kaggle.com/datasets?search='+search_term
browser.get(url) 
datasets_links = [] #top level 

#%% Search by Absolute XPath 
xpath_i = "/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[2]/div[1]/div/ul/li/a"
elems = browser.find_elements_by_xpath(xpath_i)
#elems = browser.find_elements(By.TAG_NAME, 'a') #this fetch all a links 
for elem in elems:
    href = elem.get_attribute('href')
    if href is not None:
        datasets_links.append(href)

#%% Test URLs
url_select1 = "https://www.kaggle.com/seanlahman/the-history-of-baseball" #test example1 
url_select2 = "https://www.kaggle.com/open-source-sports/baseball-databank" #test example2 

# %% Click to donwload 
#browser.get(url_select1) 
#xpath_download = "/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span"
#browser.find_elements_by_xpath(xpath_download).click()

# %% URL to download 1
browser.get(url_select1) 
browser.get(url_select1+'/download') #can only download if you signed in 


# %% URL to download 2 
browser.get(url_select2) 
browser.get(url_select2+'/download') #can only download if you signed in 


#%% Ideas 
# Not a lot of site has csv ready format - might be good to display the dataformat that they have.