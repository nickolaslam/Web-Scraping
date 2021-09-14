from typing import Text
from selenium import webdriver
import time

path = r'/usr/bin/safaridriver'


driver = webdriver.Safari(executable_path=path)
driver.get('http://www.aastocks.com/tc/forex/crypto/quote.aspx?symbol=BTCUSDT')


def getPrice(): 
    time.sleep(3)
    layout = driver.find_element_by_class_name('ct_box_1')
    text = layout.find_element_by_class_name('value').get_attribute('innerHTML')
    print('The current price is ' + text)


while True:
    getPrice()