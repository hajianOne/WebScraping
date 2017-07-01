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

        self.JobHeader = "empInfo"

        self.companyName_xpath = "//*[@id='HeroHeaderModule']/div[3]/div[2]/div/div[1]"
        
        self.jobs = []
        
        try: 
            # initialize a chrome driver without the images
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images":2}
            chromeOptions.add_experimental_option("prefs",prefs)
            
            self.browser = webdriver.Chrome(executable_path=self.driver_path,
                                            chrome_options=chromeOptions)
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
                self.clickAtCorner()
                delay = 0.75 + random.uniform(0.0,0.5)
                print "Delay:", delay
                time.sleep(delay)
            except:
                print "Could not click on the item menu"

            try:
                job = self.itemInfo()
                self.jobs.append(job)
            except:
                print "error in writing itemInfo"             

    def itemInfo(self):
        '''
        take the BasicInfo of the item selected"
        '''
        flag = False
        
        try:
            Description = self.browser.find_element_by_class_name(self.DescriptionContent)
            Description = Description.get_attribute("innerHTML")
        except:
            print "Error in itemInfo.Description"
            flag = True
        try:
            JobTitle = self.browser.find_element_by_class_name(self.JobHeader)
            JobTitle = JobTitle.find_element_by_class_name("noMargTop")
            JobTitle = JobTitle.get_attribute("innerHTML")
        except:
            print "Error in itemInfo.JobTitle"
            flag = True

        try:
            CompanyName = self.browser.find_element_by_class_name(self.JobHeader)
            
            CompanyName = CompanyName.find_element_by_class_name("empDetailsLink")
            CompanyName = CompanyName.get_attribute("innerHTML")
            
            # BasicInfo = self.browser.find_element_by_id(self.BasicInfo)
            # BasicInfo = BasicInfo.get_attribute("innerHTML")
        except:
            print "Warning in itemJob.CompanyName"
            CompanyName = None

        if flag==False:
            return Job(CompanyName, JobTitle, Description)
            
    def clickAtCorner(self):
        '''
        clicks at the corner of the page to close pop-up dialog box
        '''
        try:
            self.browser.execute_script("el = document.elementFromPoint(1,1); el.click();")
        except:
            print "Error in clickAtCorner"


    def nextpage(self):
        Footer = self.browser.find_element_by_id("FooterPageNav")
        Footer.find_element_by_class_name("next").click()
        self.clickAtCorner()
