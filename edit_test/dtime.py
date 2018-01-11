import datetime
d1 = datetime.datetime(2015, 4, 7,18,49,53)
d2 = datetime.datetime(2015, 4, 7,18,51,12)
d = (d2 - d1).seconds
print d