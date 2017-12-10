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
            time.sleep(10)

            for line in resultpc:
                if "com.financial360.nicaifu:PushClient" not in line:
                    if "com.financial360.nicaifu" in line:
                        print line
                        line = "#".join(line.split())
                        cpuinfos = line.split("#")[2].strip("%")
                        vss = line.split("#")[5].strip("K")
                        rss = line.split("#")[6].strip("K")
                        packname = line.split("#")[9]
                        mvss = int(vss)
                        mrss = int(rss)
                        vs = mvss / 1024
                        rs = mrss / 1024

                        # 将获取到的数据存到数组中
                        self.alldata.append((cpuinfos, vs, rs, packname))
                elif "com.financial360.nicaifu:PushClient" in line:
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
                    self.alldataheart.append((cpuinfosheart, vh, rh, packnameheart))
                    #ih = ih + 1

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = file('meminfo.csv','wb')
        csvfileheart = file('meminfoheart.csv','wb')
        writer = csv.writer(csvfile)
        writerheart = csv.writer(csvfileheart)
        writer.writerows(self.alldata)
        writerheart.writerows(self.alldataheart)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(2880)
    controller.testPowerCpu()
    controller.SaveDataToCSV()