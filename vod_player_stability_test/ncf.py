#encoding:utf-8
from appium import webdriver
import time
import random
import logging
from cpuNews import Controller
from popwernews import ControllerPower

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

time.sleep(10)

def testClick():
    driver.find_element_by_id("com.financial360.nicaifu:id/home_title").click()
    time.sleep(20)


while True:
    testClick()
    time.sleep(10)








