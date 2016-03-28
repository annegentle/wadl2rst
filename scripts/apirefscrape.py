#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrapes the OpenStack api-ref site for lists of operations.
"""

from lxml import html
import requests

urllist = []
page = 'http://developer.openstack.org/api-ref.html'

def get_urls_to_scrape(page):
    landing = requests.get(page)
    allpages = html.fromstring(landing.content)
    urllist = allpages.xpath('//ul[@class="nav api-sidenav"]//li/a/@href')
    print 'URLs: ', '\n'.join(urllist)
    return urllist

def scrape_url(url):
    #url = 'api-ref-compute-v2.1.html'
    page = requests.get('http://developer.openstack.org/' + url)
    tree = html.fromstring(page.content)
    #Create a list of HTTP verbs
    verbs = tree.xpath('//a[@class="operation-anchor"]/following::span[1]/text()')
    operations = tree.xpath('//a[@class="operation-anchor"]/following::div[1]/text()')
    #Match up Verbs and Operations and output a printed list
    methods = zip(verbs, operations)
    for verbs, operations in methods:
        print verbs + ' ' + operations    

def start_scrape(urllist):
    urllist = get_urls_to_scrape(page)
    for url in urllist:
        print 'URL: ', url
        print '----------'
        scrape_url(url)

get_urls_to_scrape(page)
start_scrape(urllist)

