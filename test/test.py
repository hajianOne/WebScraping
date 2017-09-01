#! /usr/bin/env python2.7

from src.glassdoor import GlassDoor

import json

Job = "Data Scientist"
City = "Berlin"

glassdoor = GlassDoor()
glassdoor.search(Job,City)

maxPage = 5

for page in range(1,maxPage+1):
    print "*** page "+ str(page) + " ***"
    glassdoor.iterateMenu()
    glassdoor.nextpage()

# writing the data as JSON file
jobs = [job.__dict__ for job in glassdoor.jobs]
with open("data/data-DS-Aug31.json", "w") as output:
    json.dump(jobs, output)

glassdoor.browser.quit()
