#/usr/bin/python
#encoding:utf-8
from appium import webdriver
import time
import os
import csv
# 1. 打开视频观看
# 2. 获取日志里的first_frametime并重定向到某个目录下
# 3. 分析并提取对应字段的值
# 4. 将提取出来的值放到csv文件中

class Controller(object):
    def __init__(self,count):
        self.start_time = [("first_frame_time")]
        self.timecount = count

    def playVideo(self):
        #点击视频观看
        while self.timecount > 0:
            cmd_result = os.popen("adb logcat | grep reportPlayStart:2117")
            #time.sleep(5)
            for line in cmd_result:
                if "first frame render time" in line:
                    print line
                    line = "=".join(line.split())
                    ftime = line.split("=")[11].strip(",")
                    self.start_time.append((ftime))

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('firsttime.csv','wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.start_time)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.testPowerCpu()
    controller.SaveDataToCSV()





