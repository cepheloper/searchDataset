import unittest
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from ds_device.scraper import displaySearch

class test_Search(unittest.TestCase):

    def setUp(self):
        self.keyword = 'Covid'
        self.ds = displaySearch(self.keyword)
    
    def tearDown(self):
        pass

    def test_kaggleSearch(self):
        kgl_url = 'https://www.kaggle.com/datasets?search=Covid'
        kgl_xpath = '//ul/li/a'
        kgl_elems = browser.find_elements_by_xpath(xpath)
        kgl_links = []        
        for elem in elems:
             kgl_links.append(elem.get_attribute('href'))
        results = self.ds.retrieveLinks()
        self.assertIn(kgl_links,results)

    def test_paths(self): 
        test_urls = self.ds.initPaths(r'\tests\test_paths.txt')
        self.assertIn('https://www.kaggle.com/datasets', test_urls)
        pass

if __name__ == '__main__':
    unittest.main()
    