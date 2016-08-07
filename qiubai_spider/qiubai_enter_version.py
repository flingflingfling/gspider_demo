# conding=utf8

import urllib
import urllib2
import re
import time
import sys


class qsbk(object):  # def the main class
    def __init__(self):  # init the class object
        self.page_index = 1  # set page_index
        self.user_agent = "Mozilla/5.0 Chrome/51.0.2704.63 Safari/537.36"  # set user_agent
        self.headers = {"User-Agent": self.user_agent}  # make headers
        self.stories = []  # gloable list which store the story

    def get_page_content(self, page_index):  # get the web content
        try:
            url = "http://www.qiushibaike.com/8hr/page/" + str(page_index)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"fail to connect web", e.reason
                return "fail code 1"
        else:
            return content

    def get_page_items(self, page_index):  # take a page content text
        page_index = self.page_index
        page_content = self.get_page_content(page_index)
        pattern = re.compile(
            u'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>.*?</span>',
            re.S)  # re method to fiad the right text
        items = re.findall(pattern, page_content)
        page_stories = []
        if items == []:
            print"sorry, some bug was happend,please restart or contact author!"
            print"this program will exit in 5 seconds."
            time.sleep(5)
            return sys.exit()
        for item in items:
            item_rp = re.compile('<br/>')
            text = re.sub(item_rp, '\n', item[1])
            page_stories.append([item[0], text.strip(), item[2], item[3]])
        return page_stories

    def load_items(self):  # make a judge for stories
        if len(self.stories) < 2:
            page_stories = self.get_page_items(self.page_index)
            self.stories.extend(page_stories)
            self.page_index += 1

    def get_one(self):
        for story in self.stories:
            # if stories <2,pull down a page_content
            inp = raw_input('type here: ')
            self.load_items()
            if inp == 'q':
                sys.exit()
            print "page number:{0}\tstory author:{1}\ncontent:{2}\ncomment number:{3}\t".format(
                self.page_index - 1, story[0], story[1], story[2], story[3])
            del self.stories[0]

    def start(self):
        print 'ready for the articles... \n"q" for the quit command,\nEnter to continue.'
        while True:
            self.load_items()
            # time.sleep(2)
            self.get_one()


qiubai = qsbk()
qiubai.start()
