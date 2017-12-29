#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time

#控制类(获取当前进程以及非主进程的CPU和内存)
class Controller(object):
    def __init__(self, count):
        self.counter = count
        #定义收集数据的数组主进程
        self.alldata = [("Draw", "Process", "Execute")]

    def testPowerCpu(self):
        while self.counter >0:
            resultpc = os.popen("adb shell dumpsys gfxinfo com.qihoo.livecloud.localserverplayer")
            self.counter = self.counter - 1
            time.sleep(3)
            for line in resultpc:
                if "" in line:
                print line
                line = "#".join(line.split())
                cpuinfos = line.split("#")[2].strip("%")



    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('meminfo.csv','wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(1)
    controller.testPowerCpu()
    controller.SaveDataToCSV()