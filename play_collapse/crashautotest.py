#/usr/bin/python
#encoding:utf-8
from appium import webdriver
import time

class Controller(object):

    def __init__(self,count):
        self.desired_caps={
                    'platformName':'Android',
                    'deviceName':'69DDU16510014677',
                    'platformVersion':'6.0',
                    'appPackage':'com.qihoo.livecloud.localserverplayer',
                    'appActivity':'com.qihoo.livecloud.MainActivity',
                    "unicodeKeyboard":"True",
                    "resetKeyboard":"True"
        }

        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.counter = count

    #之前未加延时，结果看不到滑动效果
    time.sleep(3)
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * .25)   #终点y坐标
        self.driver.swipe(x1, y1, x1, y2,t)

    def swipeDown(self,t):
        w = self.getSize()
        x1 = int(w[0] * 0.5)
        y1 = int(w[1] * 0.25)
        y2 = int(w[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(self,t):
        le = self.getSize()
        x1 = int(le[0] * 0.85)
        x2 = int(le[0] * 0.15)
        y1 = int(le[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y1, t)

    def testClick(self):
        #设置
        self.driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/setting").click()
        time.sleep(1)

    def chooseLightSky(self):
        #快视频列表
        self.driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/partner_lightsky").click()
        time.sleep(2)

    def checkVideo(self):
        #点击视频观看
        self.driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/url").click()
        time.sleep(5)

    #判断元素是否存在
    def isElementExit(self,element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_id(element)
            return flag
        except:
            flag = False
            return flag

    #初始进入列表
    def choose(self):
        count = 1
        while count >0:
            self.testClick()
            self.chooseLightSky()
            self.checkVideo()
            count = count - 1

    #崩溃后，再次进入列表
    def rechoose(self):
        recount = 1
        while recount > 0:
            self.chooseLightSky()
            self.checkVideo()
            recount = recount - 1

    def run(self):
        while self.counter > 0:
            flag = self.isElementExit("com.qihoo.livecloud.localserverplayer:id/partner_lightsky")
            if flag:
                self.chooseLightSky()
                self.checkVideo()
                self.swipeLeft(1000)
                time.sleep(5)
                self.counter = self.counter - 1
            else:
                self.swipeLeft(1000)
                time.sleep(5)
                self.counter = self.counter - 1

if __name__ == "__main__":
    controller = Controller(10)
    controller.choose()
    controller.run()
