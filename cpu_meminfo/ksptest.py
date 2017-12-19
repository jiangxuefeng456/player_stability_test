#encoding:utf-8
import time

from appium import webdriver

desired_caps={
            'platformName':'Android',
            'deviceName':'69DDU16510014677',
            'platformVersion':'6.0',
            'appPackage':'com.financial360.nicaifu',
            'appActivity':'.ui.welcome.WelcomeActivity',
            "unicodeKeyboard":"True",
            "resetKeyboard":"True"
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#之前未加延时，结果看不到滑动效果
#time.sleep(5)
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
def clickLocalServer():
    #休眠5s等待页面加载完成
    #time.sleep(5)
    #driver.find_element_by_id("com.lightsky.video:id/video_title").click()
    #driver.find_element_by_xpath("com.qihoo.livecloud.demo:index/3").click()
    driver.find_element_by_name("Local Server").click()
    time.sleep(3)

def testClick():
    #根据ID点开视频观看
    driver.find_element_by_id("com.financial360.nicaifu:id/home_title").click()
    time.sleep(20)

#clickLocalServer()

while True:
    testClick()
    time.sleep(10)

    #swipeUp(1000)
    #time.sleep(5)
    #swipeDown(1000)
    #time.sleep(5)







