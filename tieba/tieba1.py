#coding=utf-8

__author__ = 'garryforgit'

import urllib2
import re

'''
README:20160721-night
this is a python spider demo,
it's design for the freshman in the python beginner.
below is the main page about it:
http://cuiqingcai.com/993.html
http://wiki.jikexueyuan.com/project/python-crawler-guide/post.html
(i'm freshman too right now,and i just take a exercise with it.)
------------------------------------------------------------------
Get the page content like 
http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

'''

class fix_tag(object):
    ''' fix pic tag and change the /br to enter'''
    # remove img tag
    removeImg = re.compile('<img class.*?>')
    replaceline = re.compile('<tr>|<div>|</div>|</p>')
    replacehttp = re.compile('<a href=.*?>|</a>')
    replaceother = re.compile('<.*?>') # backup
    replaceTD = re.compile('<td>')
    replaceParaHead = re.compile('<p.*?>')
    replaceBr = re.compile('<br>')


    def replace(self, z):
        z = re.sub(self.removeImg, '', z)
        z = re.sub(self.replaceline, '', z)
        z = re.sub(self.replacehttp, '', z)
        z = re.sub(self.replaceTD, '\t', z)
        z = re.sub(self.replaceParaHead, '\n    ', z)
        z = re.sub(self.replaceBr, '\n', z)
        z = re.sub(self.replaceother, '', z)
        return z.strip()

class BDTB(object):
    # define the init argument
    def __init__(self, baseurl, see_lz, seprate_text):
        self.baseurl = baseurl # whicj url
        self.see_lz = '?see_lz=' + str(see_lz) # wheather to see author 1 or 0
        self.fix_tag = fix_tag()    # import fix_tag class
        self.seprate_text = seprate_text    # will the text seprate with ---
        self.defaultTitle = u'百度贴吧'
        self.floor = 1

    # get the page content according to the pagenumber
    def get_page(self, pageNum):
        try:
            url = self.baseurl + self.see_lz + '&pn' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8') # print as utf-8
        except urllib2.URLError, e:
            if hasattr(e,'reason'):
                print u'can not take the tieba content',e.reason
                return None

    # get the article title
    def get_title(self, page):
        pattern = re.compile('<h\d class=.*?title="(.*?)".*?</h\d>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None

    # get article number
    def get_all_pagenum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None

    # take all paragraph 
    def get_all_content(self, page):
        pattern = re.compile('<div id="post_content_\d+".*?>(.*?)</div>', re.S)
        result = re.findall(pattern,page)
        contents = []
        for x in result:
            # print floor,u'楼------------------------------------------------------------------------------------------------------------------------------------\n'
            # print self.fix_tag.replace(x)
            content = '\n' + self.fix_tag.replace(x) + '\n'
            contents.append(content.encode('utf-8'))
        return contents

    # name file with default title if not find title
    def set_title(self,title):
        if title is not None:
            self.file = open(title + '.md','w+')
        else:
            self.file = open(self.defaultTitle+ '.md','w+')

    def write_data(self,contents):
        for x in contents:
            if self.seprate_text == '1':
                floor_line = '\n' + str(self.floor) + u'------------------------------------------------------------------------------------------------\n'
                self.file.write(floor_line)
            self.file.write(x)
            self.floor += 1



    def start(self):
        raw_page = self.get_page(1)
        pageNum = self.get_all_pagenum(raw_page)
        title = self.get_title(raw_page)
        self.set_title(title)
        if pageNum == None:
            print 'url error,please try again'
            return 
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1,int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据"
                page_data = self.get_page(i)
                contents = self.get_all_content(page_data)
                self.write_data(contents)
        #出现写入异常
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            self.file.close()
            print "写入任务完成"

# testing page url http://tieba.baidu.com/p/3138733512

print u"请输入帖子代号"
baseurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
see_lz = raw_input("是否只获取楼主发言，是输入1，否输入0\n>>")
seprate_text = raw_input("是否写入楼层信息，是输入1，否输入0\n>>")
bdtb = BDTB(baseurl,see_lz,seprate_text)
bdtb.start() 



