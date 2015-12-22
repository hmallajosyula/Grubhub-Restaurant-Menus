
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
sys.stdout = Logger("Oakland_Menu_Level_Wave4.csv")
dataFile = open('Oakland_finalfile.txt', 'r')
out = dataFile.readlines()
global k
k=0
for number,line in enumerate(out):
#if "---" in current_line:
    if "---" in line:
        delim = line.rstrip()
        print delim

    if "Menu" in line:
       global i
       global j
       i=number
       k=k+1
       j=k
#rest_name = content.rstrip()
#newwordList = re.sub("[\b]", " ", content).split(" ")
#newwordList.pop()
#print ''.join(newwordList)

   
    regex_txt=r"(^\$)"
    if re.match(regex_txt,line) is not None:
       #prev_line = current_line[:-1]
       dollar_amount=line.rstrip()
      #print dollar_amount
       content2=out[number-1].replace(',','')
       content2=content2.rstrip()
       content3 = out[i].rstrip()
       newwordList = re.sub("[\b]", " ", content3).split(" ")
       newwordList.pop()
       print j,",",''.join(newwordList),",",content2, ",", dollar_amount
#print 'found line. the previous line is: %s' % out[number -1]


    if not line: break
dataFile.close()
