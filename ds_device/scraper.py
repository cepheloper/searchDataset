#%% Import libraries 
import logging  
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class displaySearch():
    '''Display csv datasets from listed websites based on the search term''' 

    def __init__(self, keyword):
        self.logger = self.initLogger()
        self.keyword = keyword
        self.browser = self.browserStart()


    def retrieveLinks(self):
        try:
            self.kgl_info = self.__kaggleSearch(term = self.keyword)
            self.aws_info = self.__awsSearch(term = self.keyword)
            self.writeOutput(*self.kgl_info,*self.aws_info)
        except Exception:
            self.logger.exception("Error in displaySearch")
        return [*self.kgl_info, *self.aws_info] 

    @staticmethod
    def initLogger():
        '''Initiate the log to record activity from info level'''
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('ds_device.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')      
        file_handler.setFormatter(formatter)  
        logger.addHandler(file_handler) 
        return logger

    @staticmethod
    def browserStart():
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

    def browserProfile():
        '''Apply browser profile to set download dir and disable dialogue box'''
        pass

    def __kaggleSearch(self, term = None, browser = None ): 
        '''Search for csv datasets on Kaggle and return a list of hyperlinks'''
        self.logger.info("Running __kaggleSearch")    
        if not browser:
            browser = self.browser
        kgl_links = []
        kgl_xpath = '//ul/li/a' #This is the x-path format to retrieve the hyperlinks on Kaggle
        kgl_url = 'https://www.kaggle.com/datasets'
        browser.get(kgl_url)
        search_box = '//input[contains(@class,"MuiInputBase-input")]'
        browser.find_element_by_xpath(search_box).send_keys(term)
        kgl_elems = browser.find_elements_by_xpath(kgl_xpath)
        for elems in kgl_elems:
            kgl_links.append(elems.get_attribute('href'))
        self.logger.info("__kaggleSearch returns {numResults} results".format(numResults = len(kgl_links)))
        return kgl_links

    def __awsSearch(self, term = None, browser = None): 
        '''Search for csv datasets on AWS and return a list of hyperlinks'''
        self.logger.info("Running __awsSearch")
        if not browser:
            browser = self.browser
        aws_links = []
        aws_url = 'https://registry.opendata.aws/'
        browser.get(aws_url)
        browser.find_element_by_xpath('//*[@id="search-box"]').send_keys(term)
        aws_xpath = '//div[contains(@class,"dataset") and not(@style="display:none;")]/*/a'
        aws_elems = browser.find_elements_by_xpath(aws_xpath)
        for elems in aws_elems:
            if elems.text != '': #because the site hides links which is not relevant to the search 
                aws_links.append(elems.get_attribute('href'))
        self.logger.info("__awsSearch returns {numResults} results".format(numResults = len(aws_links)))
        return aws_links

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
    
    def kaggleDownload():
        '''Download function for data from kaggle.com'''
        pass

    def awsDownload():
        '''Download function for data from aws.com'''
        pass

    
