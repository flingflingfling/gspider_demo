# oding:utf-8

import urllib2
import re
import time
import sys
from bs4 import BeautifulSoup as BSoup

‘’‘
The aim is to get all page content in iask.
1.get all pages
2.reedit page content
3.save the result into sqlite3 with pysqlite

1.1 get all url from http:
    // iask.sina.com.cn / c / 93.html - - page index increse by 111

1.2 get every index page's link:
    http:
        // iask.sina.com.cn / b / 1JJaJXiea.html
1.3 save link, question, time, content.
2.1 make page become humen read

’‘’


class ask(object):
    conn = sqlite3.connect('iask_dev.db')
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    c = conn.cursor()


# get local time
def getCurrentTime(self):
    return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))


def getCurrentDate(self):
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def main(self):
    auto_log = open('autolog.log', 'w')
    sys.stdout = auto_log
    page = open('page.txt', 'r')
    content = page.readline()
    start_page = int(content.strip()) - 1
    page.close()

# get the main tag's index page list and save to txt


def indexList(self, urls):
    f1 = open('list.txt', 'w')
    request = urllib2.Request(urls)
    response = urllib2.urlopen(request)
    pages = response.read()
    soup = BSoup(pages)  # using beautifulsoup to get url list
    rules = soup.find_all('a', target=True)
    result = list(rules)[2:-6]
    pattern = re.compile('<a href="(.*?)".*?>(.*?)</a>', re.S)
    for x in result:
        allList = re.findall(pattern, str(x))
        f1.write(allList[0][0] + '\n')
        # f1.write(allList[0][1]+'\n')
    f1.close()


# read from txt file then get the page content
def pageContent():
    f2 = open('list.txt', 'r')
    i = 0
    openlist = f2.readlines()
    assert len(openlist) != 0
    while i < len(openlist):
        url = str('http://iask.sina.com.cn' +
                  str(openlist[i]).split('\n')[0])
        i += 1
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
        assert type(content) == str
        soup = BSoup(content)
        answer = soup.find_all('pre')
        answer_times = soup.select('.answer_t')
        pattern1 = re.compile('<pre .*?>')
        pattern2 = re.compile('</pre>')
        ask1 = re.sub(pattern1, '', str(answer[0]))
        ask2 = re.sub(pattern2, '', ask1)
        answer_time1 = re.sub(pattern1, '', str(answer_times))
        answer_time = re.sub(pattern2, '', answer_time1)
        ansList = ''
        for x in answer[1:]:
            y = re.sub(pattern1, '', str(x))
            ans = re.sub(pattern2, '\n', y)
            ansList = ansList + ans + '\n'

        c.execute("INSERT INTO iask('link', 'question', 'asktime','answer') \
                  VALUES(?, ?, ?, ?)", (url, ask2, answer_time, ansList))
        conn.commit

    f2.close()


# clearfix content
def clearFix(self):
    pass

# save content into sqlite3


def saveIn(self):
    pass

# start processing


def start(self):
    pass

inp = raw_input("please input url what do you want to save in iask")
urls = str(inp)
iask = ask()
iask.start()
