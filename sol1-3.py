#coding=utf-8
#========================
# Author: Stephen chen
# Module description:  
#========================
import re
# sol0:
print 2**38
#274877906944

# sol1:
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
unveal = ''.join([chr((ord(c)-ord('a')+2) % (ord('z')-ord('a')+1)+ ord(
'a')) if c not in " .'()" else c for c in code ])
print unveal
code = "map"
unveal = ''.join([chr((ord(c)-ord('a')+2) % (ord('z')-ord('a')+1)+ ord(
'a')) if c not in " .'()" else c for c in code ])
print unveal
# 'ocr'

#sol2:
#网页源代码里面有一个大字符串，把里面的字符找出来就可以了
#先另存为文件code.txt
code = open("2.txt").read()

print "".join([c for c in code if ord(c) >= ord('a') and ord(c) <= ord('z')])


# sol3:
#先把网页源代码存出来， 题目是要求从中找一个小写字符，左右刚好各有三个大写字符的字符串。
#用re正则，这题目隐藏信息是把所有这样的小写字符组合起来，所以要用findall
a = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', open("3.txt").read())
print a
#['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']

print ''.join(a)
# 'linkedlist'






