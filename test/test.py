#! /usr/bin/env python2.7

from src.glassdoor import GlassDoor

import time

Job = "Data Scientist"
City = "Berlin"

glassdoor = GlassDoor()
glassdoor.search(Job,City)

maxPage = 2

for page in range(1,maxPage+1):
    print "*** page "+ str(page) + " ***"
    glassdoor.iterateMenu()
    glassdoor.nextpage()



# raw_input("Press a key")
glassdoor.browser.quit()
