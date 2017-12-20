#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time
# adb logcat | grep "[onError:396]" > a.txt
#控制类
class Controller(object):
    def __init__(self):
        #self.counter = count
        #定义收集数据的数组(元组必须有至少两个元素，如果一个元素的话，要在后面加上逗号,比如[("time",)])
        self.alldata = [("testNumber","ErrorTime","errorchance","resourseID","url")]

    #分析数据
    def analyzedata(self):
        #while self.counter > 0:
        content = self.readfile()
        testCount = 11.0
        errorCount = 0
        errorProbability = 0
        for line in content:
            if "onError what" in line:
                print line
                line = "12-20".join(line.split())
                videoRID = line.split("12-20")[14]
                videoURL = line.split("12-20")[16]
                print ("失败视频rid: "+videoRID)
                print ("失败视频url: "+videoURL)
                #将获取到的数据存到数组中
                errorCount = errorCount + 1

        errorProbability = errorCount / testCount
        print ("失败率: "+str(errorProbability))
        self.alldata.append((testCount,errorCount,errorProbability,videoRID,videoURL))

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('errorwhatnews.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    #读取数据文件
    def readfile(self):
        mfile = file("errorwhat.csv", "r")
        content = mfile.readlines()
        mfile.close()
        return  content

if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SaveDataToCSV()