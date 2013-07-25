#coding=utf-8
#========================
# 使用pickle, peak hell 谐音
#
#========================
import pickle
from urllib2 import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print data
for d in data:
   chars = []
   for c, num in d:
       chars.extend(c * num)
   print ''.join(chars)

# anwser is channel