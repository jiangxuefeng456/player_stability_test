#/usr/bin/python
#encoding:utf-8
import csv
import os
import time

class ControllerPower(object):
    def __init__(self, count):

        #测试的次数
        self.counter = count
        #收集数据的数组
        self.alldata = [("timestamp","power","temperate")]

    #单次测试
    def testprocess(self):
        #执行获取电量的命令
        result = os.popen("adb shell dumpsys battery")
        #i = 0
        power = 0
        temperate = 0
        #获取电量的level和当前电池的temperature
        for line in result:
            if "level" in line:
                power = line.split(":")[1]
            elif "temperature" in line:
                temperate = line.split(":")[1]

        #获取当前时间
        currenttime = self.getCurrentTime()
        #将获取到的数据存到数组中
        self.alldata.append((currenttime,power,temperate))
        #i = i +1

    #多次测试
    def run(self):
        #设置手机进入非充电状态
        #os.popen("adb shell dumpsys battery set status 1")
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter - 1
            #每20秒钟采集一次数据
            time.sleep(30)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #存储数据
    def SaveDataToCSV(self):
        csvfile = file('popwerNews.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = ControllerPower(960)
    controller.run()
    controller.SaveDataToCSV()