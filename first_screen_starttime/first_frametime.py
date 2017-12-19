#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time
# adb logcat | grep "url" > a.txt
#控制类
class Controller(object):
    def __init__(self):
        #定义收集数据的数组(元组必须有至少两个元素，如果一个元素的话，要在后面加上逗号,比如[("time",)])
        self.alldata = [("testnumber","first_render_frame_time")]

    #分析数据
    def analyzedata(self):
        content = self.readfile()
        i = 0
        for line in content:
            if "first frame render time" in line:
                print line
                line = "=".join(line.split())
                ftime = line.split("=")[11].strip(",")
                print ftime
                #将获取到的数据存到数组中
                self.alldata.append((i,ftime))
                i = i + 1

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('firstrendertime.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    #读取数据文件
    def readfile(self):
        mfile = file("firsttime.csv", "r")
        content = mfile.readlines()
        mfile.close()
        return  content

if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SaveDataToCSV()