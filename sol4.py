import urllib2
code = 12345
cnt = 0
while 1:
    page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % code).read()
    cnt += 1
    code = page.split()[-1]
    print code
    if 'going' in code:
        print page
        break

