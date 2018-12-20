import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class DouyuSelenium(unittest.TestCase):
    def __init__(self):
        '''
        初始化方法
        '''
        self.driver = webdriver.PhantomJS()
