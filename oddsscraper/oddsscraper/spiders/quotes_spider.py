#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 06:20:37 2018

@author: robinarthur
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/'                
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        



# Ajax Link: 
# https://www.wettportal.com/lib/ajax/getDatagridContent.php?lang=de&partner=wettportal&contenttype=surebets&offset=01&pagesize=78&period=all
# 2 Do:
# - get the max integer and put it into the ajax string
# - process the scraped site with all the data