#coding=utf-8
#========================
# Author: Stephen chen
# Module description:
# 网页URL后缀名改成zip，改完后会下载一个ZIP文件，打开后有一堆的txt文件，线索就在其中的一个readme.txt里：
#========================
import zipfile
code = 90052
cnt = 0
z = zipfile.ZipFile('channel.zip', mode='r')
comments = []
while 1:
    txt = "%s.txt" % code
    page = z.read(txt)
    cnt += 1
    precode = code
    code = page.split()[-1]
    print 'page:', page
    comments.append(z.getinfo(txt).comment)
    if 'comments' in page:break
    print "next code: %s" %  code
print ''.join(comments)
#小写连起来 oxygen