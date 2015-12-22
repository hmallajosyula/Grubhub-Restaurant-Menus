# Author: Harsha Mallajosyula
# MPP Candidate 2015
# Goldman School of Public Policy
# UC Berkeley
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import csv
import os
import sys
import logging
import random
import time
import codecs
import datetime
from time import strftime

#writing to text file
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

#sys.stdout = Logger("log_lastname_I_HM.csv")
sys.stdout = Logger(strftime("Logfiles/Livermore_Restaurant_Menus_%H_%M_%m_%d_%Y.txt"))


#setting proxy server
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "proxy.server.address")
profile.set_preference("network.proxy.http_port", "port_number")
profile.update_preferences()
br = webdriver.Firefox(firefox_profile=profile)
br.implicitly_wait(15) # wait's for the page to get done loading before it does anything with it
br.get('https://www.grubhub.com/search?orderMethod=pickup&locationMode=PICKUP&facetSet=umami&pageSize=20&latitude=37.68187332&longitude=-121.76800538&radius=3&countOmittingTimes')
time.sleep(30)
br.implicitly_wait(15)
br.switch_to_default_content()

for i in range(1,20):
    try:
        
        time.sleep(15)
        br.find_element_by_xpath('//*[@id="ghs-search-results-container"]/div[2]/div/div/div/div[1]/div[3]/div['+str(i)+']//a[@class="restaurant-name s-link"]').click()
                                 #br.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[6]/div[3]/ul/li['+str(i)+']//a[@class="link-to-search-result slides-above-the-showcase open-restaurant online-ordering-restaurant"]').click()
        time.sleep(15)
        el4 = br.find_element_by_xpath('//*[@id="ghs-outerWrapper"]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/h1/span')
        el4 = el4.text.encode('utf8')
        print '----------------------------------------------------\n'
        print 'Restaurant Name and Menu Items: \n'
        print el4
        time.sleep(15)
        el5 = br.find_element_by_xpath('//*[@id="ghs-outerWrapper"]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div')
        el5 = el5.text.encode('utf8')
        time.sleep(15)
        print el5
        print 'Restaurant Contact Info and Address \n'
        el6 = br.find_element_by_xpath('//*[@id="ghs-outerWrapper"]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]')
        el6 = el6.text.encode('utf8')
        print el6
        print '-----------------------------------------------------\n'
        i = i + 1;
        br.back();
    except NoSuchElementException:
        br.implicitly_wait(45)
        print ("Error loading page")
        seconds = 10 + (random.random()*5)
        time.sleep(seconds)
        i = i+1;
        br.back();
    except ElementNotVisibleException:
        br.implicitly_wait(45)
        seconds = 10 + (random.random()*5)
        time.sleep(seconds)
        break




br.quit()





