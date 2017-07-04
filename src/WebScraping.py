#! /usr/bin/env python2.7

'''
WebScraping.py contains classes relevant for a single readout of a webpage.


@author Soheil Hajian
@version 1.0
'''

from warnings import warn 


class ScrapedPage(object):
    '''
    class ScrapedPage represents a page on the web which is scrapped.
    '''

    def __init__(self, url, date, html):
        '''
        initiate an instance of the scraped page.
        '''

        self.url  = url
        self.date = date
        self.html = html


class Job(object):
    '''
    class Job contains information of the job retrieved.
    '''
    def __init__(self, company, job, description, link=""):

        self.company = company
        self.job = job
        self.description = description
        self.link = link

    def info(self):
        print "Company: ", self.company
        print "Job Title: ", self.job

