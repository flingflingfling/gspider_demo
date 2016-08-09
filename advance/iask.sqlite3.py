# coding=utf-8

import sqlite3

'''this just the simply python-sqlite3 operate '''

conn = sqlite3.connect('iask_dev.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS iask(id INTEGER PRIMARY KEY AUTOINCREMENT,link CHAR(254) NOT NULL,question TEXT NOT NULL,asktime char NOT NULL,answer TEXT NOT NULL)''')

c.execute("""INSERT INTO IASK VALUES ('1','OWO23SDF.HTML','how to manage sqlite3 in python?','2014-07-07 12:12:12','just read the original source code,just kidding!you should copy some code and understand it ,then pratice and pratice and pratice!')""")

conn.commit()

c.close()


