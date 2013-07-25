#coding=utf8
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#  打开源代码，用urllib2 follow每一个页面，里面会提示，打印出来， 一步步走下去
#
#
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
import urllib2
code = 12345
cnt = 0
while 1:
    page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % code).read()
    cnt += 1
    precode = code
    code = page.split()[-1]
    print 'page:', page
    if "Yes. Divide by two and keep going." in page:
        print "follow prompt"
        code = str(int(precode) / 2)

    if "misleading" in page:
        print 'follow'

    if 'html' in page:
        break

    print "next code: %s" %  code
    if cnt > 400: break

#Anwser: http://www.pythonchallenge.com/pc/def/peak.html
