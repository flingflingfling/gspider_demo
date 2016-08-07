#coding=utf-8

import urllib
import urllib2
import re

page = 1
url = "http://www.qiushibaike.com/8hr/page/" + str(page)
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
headers = { "User-Agent" : user_agent}

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)

    content = response.read()
    #contents = urllib2.unquote(content)
    pattern = re.compile(u'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>.*?</span>', re.S)
    items = re.findall(pattern,content)
    for item in items:
        print 'author: '+item[0],item[1],'funny num:'+item[2],'comment num:'+item[3]
except Exception, e:
    e
