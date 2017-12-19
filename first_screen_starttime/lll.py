#-*-coding:utf-8-*-
import csv
import re
import time
import subprocess

class Controller_time(object):
    def __init__(self):
        self.data = [("video_url","render_time")]
#一定时间内执行adb logcat命令,并将日志保存在本地文件中。
    def save_log(self):
        filename = "E:/log.txt"
        logcat_file = open(filename,'w+')
        logcmd = 'adb logcat | findstr "first frame render time" '
        Poplog = subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE,shell=True)
        time.sleep(20)
        Poplog.terminate()
        logcat_file.close()
#从本地文件中读取日志，过滤日志。
    def get_useful_log(self):
        log_data =file('E:/log.txt','r')
        data = log_data.readlines()
        log_data.close()
        while '' in data:
            data.remove('')
        for line in data:
            if "first frame render time" in line:
                useful_log = open("E:/useful_log.txt",'a')
                useful_log.write(line)
                useful_log.close()

#从文件中获取url和首屏时间
    def get_data(self):
        useful_data = file('E:/useful_log.txt','r')
        data = useful_data.readlines()
        useful_data.close()
        for line in data:
            ll = line.split()
            time = ll[10]
            url = ll[11]
            print(url)
            print(time)
            self.data.append((url,time))

#存储数据
    def save_data(self):
        csvfile = file("render_time","wb")
        writer = csv.writer(csvfile)
        writer.writerows(self.data)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller_time()
    controller.save_log()
    controller.get_useful_log()
    controller.get_data()
    controller.save_data()


