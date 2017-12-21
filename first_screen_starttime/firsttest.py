#/usr/bin/python
#encoding:utf-8
from appium import webdriver
import time

desired_caps={
            'platformName':'Android',
            'deviceName':'69DDU16510014677',
            'platformVersion':'6.0',
            'appPackage':'com.qihoo.livecloud.localserverplayer',
            'appActivity':'com.qihoo.livecloud.MainActivity',
            "unicodeKeyboard":"True",
            "resetKeyboard":"True"
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#之前未加延时，结果看不到滑动效果
time.sleep(3)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * .25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

def swipeDown(t):
    w = getSize()
    x1 = int(w[0] * 0.5)
    y1 = int(w[1] * 0.25)
    y2 = int(w[1] * 0.75)
    driver.swipe(x1, y1, x1, y2, t)

def swipeLeft(t):
    le = getSize()
    x1 = int(le[0] * 0.85)
    x2 = int(le[0] * 0.15)
    y1 = int(le[1] * 0.5)
    driver.swipe(x1, y1, x2, y1, t)

def testClick():
    #设置
    driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/setting").click()
    time.sleep(1)

def chooseLightSky():
    #快视频列表
    driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/partner_lightsky").click()
    time.sleep(2)

def checkVideo():
    #点击视频观看
    driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/url").click()
    time.sleep(5)

def clickBack():
    #返回到列表页
    driver.find_element_by_id("com.qihoo.livecloud.localserverplayer:id/iv_header_left").click()
    time.sleep(2)

count = 1
while count >0:
    testClick()
    chooseLightSky()
    time.sleep(15)
    checkVideo()
    count = count - 1

testCount =300
while testCount>0:
    swipeLeft(1000)
    time.sleep(10)
    testCount = testCount - 1


