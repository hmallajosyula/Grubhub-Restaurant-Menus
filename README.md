# Grubhub-Restaurant-Menus
This repo includes code to scrape and clean Restaurant Menus from Grubhub 

This coding project was part of my quantitative analysis for my Masters Thesis at UC Berkeley. The scope of the project was to quantify the price response of restaurants in Oakland to a 36 percent increase in minimum wage.

The statistical design implements a difference-in-difference strategy where the treatment group is Oakland and the Control group is surrounding cities in the East Bay. 

The code included here scrapes restaurant menus present in Oakland and the control to generate a csv file of restaurant menus. 

Code written to clean the scraped data is in the folders:
Logfiles\Control\ItemLevel
Logfiles\Oakland\ItemLevel

All of the code is written in Python.2.7.

Selenium module is required to run webscraping.It can be installed on mac using the following command: pip install selenium