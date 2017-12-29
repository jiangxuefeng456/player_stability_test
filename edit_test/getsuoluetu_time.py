# encoding: utf-8
import csv
import datetime
# 获取缩略图合成时长
class Controller(object):
    def __init__(self):
        self.alltimedata = [("i","composetime")]
        self.totime = "12-26"

    #分析数据
    def analyzeDateTime(self):
        content = self.readTimeline()
        startTime = 0
        endTime = 0
        i = 1
        for line in content:
            if "video_edit_new_thumbnail max_mem_cache_num" in line:
                startline = self.totime.join(line.split())
                startTime = startline.split(self.totime)[1]
                print ("开始时间："+startTime)
            if "thumbnail_process exit" in line:
                endline = self.totime.join(line.split())
                endTime = endline.join(self.totime)[1]
                print ("结束时间："+endTime)
            allTime = (endTime-startTime).seconds
            print allTime
            self.alltimedata.append((i,allTime))
            i = i+1

    #存储数据
    def saveDateTime(self):
        timefile = file("sltcompose.csv","wb")
        csvfile = csv.writer(timefile)
        csvfile.writerows(self.alltimedata)
        timefile.close()


    #读取数据文件
    def readTimeline(self):
        sltfile = file("slttime.csv","r")
        timeContent = sltfile.readlines()
        sltfile.close()
        return timeContent