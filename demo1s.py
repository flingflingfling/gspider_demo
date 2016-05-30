#coding=utf-8

import urllib2


url = "http://cn.bing.com"

response =urllib2.urlopen(url)

print response.read()
