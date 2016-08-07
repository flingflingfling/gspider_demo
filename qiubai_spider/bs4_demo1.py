#coding:utf-8

from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
#soup = BeautifulSoup(open('index.html')) #using local html as object

#print soup.prettify()
print "the title is {},and head is {}" .format(soup.title.string,soup.head.string)

print soup.a
print soup.p
print soup.p.get('class') #using get method
print soup.p.string

