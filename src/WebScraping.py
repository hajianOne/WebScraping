#! /usr/bin/env python2.7

'''
WebScraping.py contains classes relevant for a single readout of a webpage.


@author Soheil Hajian
@version 1.0
'''

from warnings import warn 


class ScrapedPage(object):
    '''
    class ScrapedPage represents a page on the web which is scrapped
    '''

    def __init__(self, url, date, html):
        '''
        initiate an instance of the scraped page.
        '''

        self.url  = url
        self.date = date
        self.html = html


