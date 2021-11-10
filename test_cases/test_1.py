# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :test_1.py
import time
import unittest
from selenium import webdriver


class TestOpen(unittest.TestCase):

    def test_1(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        time.sleep(10)

    def test_2(self):
        print("这是第二个用例")











