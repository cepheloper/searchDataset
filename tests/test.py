import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from scraper import displaySearch

class test_display(unittest.TestCase):

    def test_browser(self):
        '''Test if browser responds'''
        pass

    def test_kaggleSearch(self):
        '''Check if kaggle dataset url is returning expected searched value'''
        kgl_url = 'https://www.kaggle.com/datasets?search=baseball'
        kgl_xpath = '//ul/li/a'
        kgl_elems = browser.find_elements_by_xpath(xpath)
        for elem in elems:
            if elem.get_attribute('href') == 'https://www.kaggle.com/seanlahman/the-history-of-baseball':
                self.assertTrue


if __name__ == '__main__':
    unittest.main()
