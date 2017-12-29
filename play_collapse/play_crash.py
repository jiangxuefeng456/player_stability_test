#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time
# adb logcat -s AndroidRuntime > asd.txt
#控制类
class Controller(object):
    def __init__(self):
        self.alldata = [("crashTime","crashChance")]

    #分析数据
    def analyzedata(self):
        content = self.readfile()
        crashCount = 0
        crashProbability = 0
        for line in content:
            if "java.lang.RuntimeException" in line:
                #print line
                line = "/".join(line.split())
                crashtime = line.split("/")[1]
                print ("崩溃时间: "+crashtime)
                #将获取到的数据存到数组中
                crashCount = crashCount + 1

        crashProbability = crashCount / 100.0
        print ("崩溃率: "+str(crashProbability))
        self.alldata.append((crashtime,crashProbability))

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('crashnews.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    # 读取数据文件
    def readfile(self):
        mfile = file("crash.csv", "r")
        content = mfile.readlines()
        mfile.close()
        return content

if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SaveDataToCSV()