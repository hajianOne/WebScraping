#! /usr/bin/env python2.7

from warnings import warn
from selenium import webdriver

import time
import random

class Job(object):

    def __init__(self, company, job, description, link=""):

        self.company = company
        self.job = job
        self.description = description
        self.link = link

    def info(self):
        print "Company: ", self.company
        print "Job Title: ", self.job
        # print "Description:"
        # print self.description
        
class GlassDoor(object):

    def __init__(self):
        '''
        Initialize an instance for GlassDoor scrapping.
        '''
        self.homeUrl     = "https://www.glassdoor.de/index.htm"
        self.driver_path = "/usr/lib/chromium-browser/chromedriver"

        self.searchID   = "KeywordSearch"
        self.locationID = "LocationSearch"
        self.submitID   = "HeroSearchButton"

        self.MainList_xpath = "//*[@id='MainCol']/div/ul/li"

        self.BasicInfo = "BasicInfo"

        self.DescriptionContent = "jobDescriptionContent"
        self.jobTitle_xpath = "//*[@id='HeroHeaderModule']/div[3]/div[2]/h2"
        self.companyName_xpath = "//*[@id='HeroHeaderModule']/div[3]/div[2]/div/div[1]"
        
        self.jobs = []
        
        try: 
            self.browser = webdriver.Chrome(executable_path=self.driver_path)
            try:
                self.browser.get(self.homeUrl)
            except:
                warn("Error in GlassDoor class __init__: URL is not loaded")
        except:
            warn("Error in GlassDoor class __init__: browser is not loaded")

    def home(self):
        try:
            self.browser.get(self.homeUrl)
        except:
            warn("Error in home")
            
    def search(self, job, city, category="job"):
        '''
        search performs a search on the main page.
        '''
        self.job  = job
        self.city = city

        SearchForm = self.browser.find_element_by_id(self.searchID)
        SearchForm.clear()
        SearchForm.send_keys(job)

        LocationSearch = self.browser.find_element_by_id(self.locationID)
        LocationSearch.clear()
        LocationSearch.send_keys(city)

        SubmitButton = self.browser.find_element_by_id(self.submitID)
        SubmitButton.click()


    def iterateMenu(self):
        '''
        iterateMenu iterates over the main items of the search results.
        '''
        items = self.browser.find_elements_by_xpath(self.MainList_xpath)

        for item in items:
            try:
                item.click()
                
                delay = 1.0 + random.uniform(0.0,2.0)
                print "Delay:", delay
                time.sleep(delay)
                
                self.jobs.append( self.itemInfo() )
            except:
                print "Could not click on the item menu"

    def itemInfo(self):
        '''
        take the BasicInfo of the item selected"
        '''

        try:
            Description = self.browser.find_element_by_class_name(self.DescriptionContent)
            Description = Description.get_attribute("innerHTML")
            
            JobTitle = self.browser.find_element_by_xpath(self.jobTitle_xpath)
            JobTitle = JobTitle.get_attribute("innerHTML")
            
            CompanyName = self.browser.find_element_by_xpath(self.companyName_xpath)
            CompanyName = CompanyName.get_attribute("innerHTML")
            
            BasicInfo = self.browser.find_element_by_id(self.BasicInfo)
            BasicInfo = BasicInfo.get_attribute("innerHTML")
            
            return Job(CompanyName, JobTitle, Description)
        except:
            print "Could not read"
        
