#encoding:utf-8
from appium import webdriver
import time
import random
import logging

desired_caps={
            'platformName':'Android',
            'deviceName':'69DDU16510014677',
            'platformVersion':'6.0',
            'appPackage':'com.qihoo.livecloudrefactor',
            'appActivity':'.MainActivity',
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

def testClick():
    #点击视频编辑
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/btn_video_edtior").click()
    time.sleep(1)

def chooseFile():
    #选择文件
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/choose_file").click()
    time.sleep(2)

def checkPicture():
    #选择图片
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/check").click()
    time.sleep(2)

def checkDone():
    #已完成选择
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/picture_tv_ok").click()
    time.sleep(4)

def editPicture():
    #执行编辑操作：剪切
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/edit_cut").click()
    time.sleep(3)

def tiePicture():
    # 加音乐
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/edit_set_music").click()
    time.sleep(2)

def playPicture():
    #播放
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/edit_play").click()
    time.sleep(8)

def playExport():
    #导出文件
    driver.find_element_by_id("com.qihoo.livecloudrefactor:id/edit_export").click()

    time.sleep(60)

def backClick():
    # 手机虚拟键返回
    driver.keyevent(4)
    time.sleep(2)

count = 2
while count>0:
    swipeUp(1000)
    count = count - 1

clickCount = 1
while clickCount>0:
    testClick()
    clickCount = clickCount - 1

testCount =30
while testCount>0:
    chooseFile()
    checkPicture()
    checkDone()
    editPicture()
    #tiePicture()
    playPicture()
    playExport()
    backClick()
    testCount = testCount - 1






