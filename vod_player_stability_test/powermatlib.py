#!/usr/bin/python
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import sys

power360 = ""
alipower = ""
path=r"C:\Users\jiangxuefeng\Desktop\powers\ali360power.csv"


#折线图
fig = plt.figure()
plt.subplot(122)
plt.plot(power360,color='b',label="360")
plt.plot(alipower,color='c',label="ali")
plt.xlabel("time",fontsize='x-large')
plt.ylabel("power(%)",fontsize='x-large')
plt.legend(ncol=2,loc=0)
plt.title("The trend of launchtimeinfo",fontsize='xx-large')
plt.savefig("launchtimeinfo.png")
plt.show()
