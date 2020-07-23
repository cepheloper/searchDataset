#%% Import libraries 
import logging  
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxProfile

class displaySearch():
    '''Display csv datasets from listed websites based on the search term''' 

    def __init__(self, keyword):
        self.logger = self.__initLogger()
        self.keyword = keyword
        self.browser = self.__browserStart()
        self.initPaths()
        self.checkUrl()

    def retrieveLinks(self):
        '''Search datasets on different websites. Paths.txt must be filled to utilize the attributes'''
        try: #Add paths to search in the following format 
            self.kgl_info = self.__Search(term = self.keyword, url = self.kgl_url, linksPath = self.kgl_xpath, searchBoxPath = self.kgl_box)
            self.aws_info = self.__Search(term = self.keyword, url = self.aws_url, linksPath = self.aws_xpath, searchBoxPath = self.aws_box)
        except Exception:
            self.logger.exception("Error in displaySearch")
        return [*self.kgl_info, *self.aws_info] # Do not forget to return the values after paths are added 

    def initPaths(self):
        self.urls = []
        with open("paths.txt", encoding='utf-8') as f:
            for line in f:
                key, value = line.rstrip("\n").split("***")
                setattr(self, key, value)
                if 'url' in key: 
                    self.urls.append(value)

    @staticmethod
    def __initLogger():
        '''Initiate the log to record activity from info level'''
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('ds_device.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')      
        file_handler.setFormatter(formatter)  
        logger.addHandler(file_handler) 
        return logger

    @staticmethod
    def __browserStart():
        opts = Options()
        opts.headless = True
        browser = Firefox(options=opts)
        return browser

    @staticmethod
    def writeOutput(*weblinks):
        outs = open("output.txt" , "w")
        for link in weblinks: 
            outs.write(link)
            outs.write("\n")
        outs.close

    def __Search(self, url, searchBoxPath, linksPath, term = None, browser = None ):
        self.logger.info("Running search on {website}".format(website = url)) 
        if not browser:
            browser = self.browser
        searchResults = []
        browser.get(url)
        browser.find_element_by_xpath(searchBoxPath).send_keys(term)
        elements = browser.find_elements_by_xpath(linksPath)
        for elems in elements:
            searchResults.append(elems.get_attribute('href'))
        self.logger.info("Search on {searchTitle} returns {numResults} results".format(searchTitle = url, numResults = len(searchResults)))
        return searchResults

    def downloadKaggle(self,link,browser = None):
        if not browser: 
            browser = self.browser
        try:
            browser.get(link+'/download')
        except: 
            self.logger.exception("Error in download function")

    def checkUrl(self):
        for url in self.urls: 
            try: 
                response =  requests.get(url)
                if response.ok:
                    self.logger.info('Connection to {urlx} can be established.'.format(urlx = url))
            except: 
                    self.logger.error('Connection to {urlx} cannot be established'.format(urlx = url))


class downloadData():
    '''Download datasets from the search results'''

    def __init__(self):
        pass

    def selectDir(self):
        '''Select directory to download the data to by setting browser settings'''
        pass

    def webIdentifier():
        '''Identify the datasource e.g. aws or kaggle , to determine the download functions required'''
        pass
    
    

    
