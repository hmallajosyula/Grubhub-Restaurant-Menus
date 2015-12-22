
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
sys.stdout = Logger("Control_Restaurant_Minorder_Post.csv")
dataFile = open('Control_finalfile.txt', 'r')
while True:
   content  = dataFile.readline()
   #wordList = re.sub("[\b]", " ", content).split(",")
   content = filter(None, content)
   
   if "DELIVERY" in content:
       #min_amount = content.rstrip()
      content2= dataFile.readline()
      content2= dataFile.readline()
      content2=content2.rstrip()
      #print content2
      newwordList = re.sub("[\b]", " ", content2).split(" ")
      newwordList = newwordList.pop()
      #min_amount = min_amount.pop()
      print newwordList


#elif "FEMALE" in newwordList:
      #gender = 'FEMALE'

#int_list = [int(s) for s in re.findall('\\d+', str(newwordList))]
   if not content: break
dataFile.close()
