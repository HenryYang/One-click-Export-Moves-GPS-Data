# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import datetime
import time
import os
import sys
t = time.time()

a = (raw_input('Please Enter the start date:'))

try:
  cookie = open('cookie.txt')
  cookiedata = cookie.read()
except IOError:
  print 'Please enter your cookie to cookie.txt FIRST'
  open('cookie.txt','a')


yt = int(a[:4])
mt = int(a[4:6])
dt = int(a[6:8])



i=0
while 1>0:
  d0=datetime.datetime(yt,mt,dt)
  d1=d0 + datetime.timedelta(days =i)
  d2=d1.strftime('%Y%m%d')
  i=i+1
  url1 ='http://www.moves-export.com/gpxactivity?type=storyline&destination=dropbox&startdate='
  print url1+d2
  cookies = dict(ACSID=cookiedata)
  r = requests.get(url1+d2, cookies=cookies)
  od0y = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d')
  if d2 == od0y:
    break


