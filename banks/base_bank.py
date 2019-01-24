"""
by Zhixuan Wang
2019-01-23
"""

from selenium import webdriver

class BaseBank(object):

    def __init__(self, username, password, url):
        self.authtentication={
            'username': username,
            'password': password
        }
        self.url = url
        self.wd = webdriver.Chrome()
        self.wd.get(self.url)

    def get_transactions(self):
        raise NotImplementedError

