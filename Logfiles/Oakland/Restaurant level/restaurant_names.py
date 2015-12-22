
#Author: Harsha Mallajosyula

import string
import re
import csv
import os
import sys
import logging
import random
import time

#writing to text file
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
    
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

#sys.stdout = Logger(".csv")
sys.stdout = Logger("Oakland_Restaurant_Names.csv")
dataFile = open('Oakland_finalfile.txt', 'r')
while True:
   content  = dataFile.readline()
   #wordList = re.sub("[\b]", " ", content).split(",")
   content = filter(None, content)
   #newwordList = re.sub("[\b]", " ", content1).split(" ")
   #newwordList = wordList[1].split(" ")
   #newwordList = filter(None, newwordList

   if "Menu" in content:
      rest_name = content.rstrip()
      newwordList = re.sub("[\b]", " ", content).split(" ")
      newwordList.pop()
      print ''.join(newwordList)

#print min_amount

#elif "FEMALE" in newwordList:
      #gender = 'FEMALE'

#int_list = [int(s) for s in re.findall('\\d+', str(newwordList))]

   if not content: break
dataFile.close()
