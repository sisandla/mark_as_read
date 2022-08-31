from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
import itertools
from time import sleep
import parameters
from csv import DictReader

from fake_useragent import UserAgent

class MarkAsReadCrawler():

    def __init__(self):
        # options = webdriver.FirefoxOptions()
        self.driver = webdriver.Chrome()
        # safari_UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15'
        # UA = 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'

    def get_cookie_data(self, path):
        data_frame = pd.read_csv(path)

        return data_frame


    def cookies(self, data):
        df = pd.read_csv(COOKIES)
        df = df[df.eq(data).any(axis=1)]
        if df.empty:
            return False
        else:
            return True


    def bypass_login(self):
        addrs_query = self.driver.find_element(By.ID, 'identifierId')
        addrs_query.send_keys(parameters.gmail_address)
        next_click = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_click.click()
    

    def get_cookie_values(self, file):
        dictionary_ = {}
        with open(file) as f:
            read = DictReader(f)
            # read_res = pd.Series(read).loc[l].to_dict()
            dictionary_ = list(read)
        return dictionary_



    def _start(self):
        COOKIES = ("cookie_data.csv")
        _helper_link = 'https://mail.google.com/mail/u/1/#inbox'
        self.driver.get(_helper_link)
        self.driver.implicitly_wait(5)
        # print(self.get_cookie_data(COOKIES))
        cookies = self.get_cookie_values(COOKIES)
        for item in cookies:
            indx = ['name', 'value', 'domain']
            _cookies = {key: item[key] for key in indx}
            print(_cookies)
            self.driver.add_cookie(_cookies)
            self.driver.refresh()
        try:
            # self.get_cookie_values(COOKIES)
            # self.get_cookie_data(COOKIES)
            # print(self.get_cookie_values(COOKIES))
            sleep(10)
            self.driver.close() 
        except:
            print('quitting!')
            self.driver.close()


if (__name__ == "__main__"):
    crawl = MarkAsReadCrawler()
    # login here


    # start crawling
    crawl._start()