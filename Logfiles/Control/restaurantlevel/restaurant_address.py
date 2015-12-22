
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
sys.stdout = Logger("Control_Restaurant_Address_POST.csv")
dataFile = open('Control_finalfile.txt', 'r')
while True:
   content  = dataFile.readline()
   #wordList = re.sub("[\b]", " ", content).split(",")
   content = filter(None, content)
   #newwordList = re.sub("[\b]", " ", content1).split(" ")
   #newwordList = wordList[1].split(" ")
   #newwordList = filter(None, newwordList

   if ", CA" in content:
      address = content.rstrip()
      print address

   #elif "FEMALE" in newwordList:
      #gender = 'FEMALE'

   if not content: break
dataFile.close()
