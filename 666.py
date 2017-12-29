#/usr/bin/python
#encoding:utf-8
import re

file = 'd:/gf.txt'
datas = []

w1 = 'Draw	Prepare	Process	Execute'
w2 = 'Stats since'

f = open(file,'r')
buff = f.read()
a = re.search('(<cert>\s+)(.*)(\s+</cert>)', buff, re.S).group(2)
print a