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
        self.alldata = [("cpuinfo", "vss", "rss", "packagename")]
        #定义手机数据的数组心跳进程
        self.alldataheart= [("cpuinfoheart", "vssheart", "rssheart", "packagenameheart")]

    def testPowerCpu(self):
        while self.counter >0:
            resultpc = os.popen("adb shell top -m 500 -n 1 -s cpu")
            self.counter = self.counter - 1
            time.sleep(30)

            for line in resultpc:
                if "com.qihoo.livecloudrefactor" in line:
                    print line
                    line = "#".join(line.split())
                    cpuinfosheart = line.split("#")[2].strip("%")
                    vssheart = line.split("#")[5].strip("K")
                    rssheart = line.split("#")[6].strip("K")
                    packnameheart = line.split("#")[9]
                    mvh = int(vssheart)
                    vh = mvh / 1024
                    mrh = int(rssheart)
                    rh = mrh / 1024

                    # 将获取到的心跳数据存到数组中
                    #self.alldataheart.append((cpuinfosheart, vh, rh, packnameheart))
                    #ih = ih + 1

    #数据的存储
    def SaveDataToCSV(self):
        #csvfile = file('meminfo.csv','wb')
        csvfileheart = file('jianjimem.csv','wb')
        #writer = csv.writer(csvfile)
        writerheart = csv.writer(csvfileheart)
        #writer.writerows(self.alldata)
        writerheart.writerows(self.alldataheart)
        csvfileheart.close()

if __name__ == "__main__":
    controller = Controller(50)
    controller.testPowerCpu()
    controller.SaveDataToCSV()