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
        self.dataerror = [("testNumber","ErrorTime","errorchance","resourseID","url")]
        self.alldataerror = []

    #分析数据
    def analyzedata(self):
        content = self.readfile()
        testCount = 180.0 #测试次数
        itime = 1
        ftime = 0
        errorCount = 0
        videoRID = 0
        videoURL = 0
        errorProbability = 0 #失败率

        for line in content:
            if "onError what" in line:
                print line
                line = "12-21".join(line.split())
                videoRID = line.split("12-21")[14]
                videoURL = line.split("12-21")[16]
                print ("失败视频rid: " + videoRID)
                print ("失败视频url: " + videoURL)
                errorCount = errorCount + 1
                errorProbability = errorCount / 180.0
                self.dataerror.append((testCount, errorCount, errorProbability, videoRID, videoURL))

            elif "first frame render time" in line:
                print line
                line = "=".join(line.split())
                ftime = line.split("=")[11].strip(",")
                print ftime
                #将获取到的数据存到数组中
                self.alldata.append((itime,ftime))
                itime = itime + 1

        print ("失败率: " + str(errorProbability))
        for errorvalue in self.dataerror:
            self.alldataerror.append(errorvalue)

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('firstrendertime.csv', 'wb')
        csvfileerror = file('errortime.csv','wb')
        writer = csv.writer(csvfile)
        writererror = csv.writer(csvfileerror)
        writer.writerows(self.alldata)
        writererror.writerows(self.alldataerror)
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