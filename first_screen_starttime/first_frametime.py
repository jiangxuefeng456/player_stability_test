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
        self.alldata = [("testnumber","first_render_frame_time","rid")]
        self.dataerror = [("testNumber","ErrorTime","errorchance","resourseID","url")]
        self.alldataerror = []
        self.rid = []
        self.date = "12-27"

    #分析数据
    def analyzedata(self):

        content = self.readfile()
        testCount = 350.0 #测试次数
        itime = 1  #视频播放次数
        ftime = 0  #视频播放首帧时间
        errorCount = 0 #播放失败次数
        videoRID = 0  #播放失败视频的rid
        videoURL = 0  #播放失败视频的URL
        errorProbability = 0 #播放失败率
        frid = " "   #获取首帧时间时，对应的视频rid
        furl = 0
        for line in content:
            #视频播放失败
            if "onError what" in line:
                print line
                line = self.date.join(line.split())
                videoRID = line.split(self.date)[14]
                videoURL = line.split(self.date)[16]
                print ("失败视频rid: " + videoRID)
                print ("失败视频url: " + videoURL)
                errorCount = errorCount + 1
                errorProbability = errorCount / testCount
                self.dataerror.append((testCount, errorCount, errorProbability, videoRID, videoURL))

            #播放视频对应的rid，存储到数组中
            elif "startPlay rid" in line:
                self.rid.append(line)

            elif "first frame render time" in line:
                print line
                line = self.date.join(line.split())
                ftime = line.split(self.date)[11].strip(",").lstrip("time=")
                furl = line.split(self.date)[12]
                print ("视频首帧时间: " + str(ftime))
                for line in self.rid:
                    line = self.date.join(line.split())
                    ridurl = line.split(self.date)[10]
                    if ridurl == furl:
                        frid = line.split(self.date)[9].strip(",")
                        print ("视频对应rid: " + frid)
                #将获取到的数据存到数组中
                self.alldata.append((itime,ftime,frid))
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