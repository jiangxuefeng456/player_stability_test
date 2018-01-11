#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time
import datetime

#  adb logcat -s VIDEO_EDIT > e.txt
#控制类
class Controller(object):
    def __init__(self,count):
        #定义收集数据的数组(元组必须有至少两个元素，如果一个元素的话，要在后面加上逗号,比如[("time",)])
        self.alldata = [("startTime",)]
        self.date = "."
        self.counter = count

    #分析数据
    def analyzedata(self):
        while self.counter>0:
            startTime = " "
            line1 = " "
            hours = " "
            minutes = " "
            secon = " "
            s = ""
            e = ""
            endTime = " "
            line2 = " "
            ehours = " "
            eminutes = " "
            esecon = " "
            zTime = " "
            editTime = os.popen("adb logcat -s VIDEO_EDIT")
            # content = self.readfile()
            for line in editTime:
                # 视频播放失败
                if "video_edit_muxing_process enter" in line:
                    print line
                    line = self.date.join(line.split())
                    startTime = line.split(self.date)[1]
                    line1 = ":".join(startTime.split())
                    hours = line1.split(":")[0]
                    minutes = line1.split(":")[1]
                    secon = line1.split(":")[2]
                    s = datetime.datetime(2018, 1, 11, int(hours), int(minutes), int(secon))
                    print ("时分秒: " + str(s))
                if "video_edit_process exit" in line:
                    print line
                    line = self.date.join(line.split())
                    endTime = line.split(self.date)[1]
                    line2 = ":".join(endTime.split())
                    ehours = line2.split(":")[0]
                    eminutes = line2.split(":")[1]
                    esecon = line2.split(":")[2]
                    e = datetime.datetime(2018, 1, 11, int(ehours), int(eminutes), int(esecon))
                    print ("后时分秒：" + str(e))
                    zTime = (e - s).seconds
                    print zTime
                    self.alldata.append((zTime,))
                    csvfile = file('startEndtime.csv', 'wb')
                    writer = csv.writer(csvfile)
                    writer.writerows(self.alldata)
                    csvfile.close()
                    self.counter = self.counter - 1

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('startEndtime.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    #读取数据文件
    def readfile(self):
        mfile = file("muxing.csv", "r")
        content = mfile.readlines()
        mfile.close()
        return  content

if __name__ == "__main__":
    controller = Controller(3)
    controller.analyzedata()
    #controller.SaveDataToCSV()