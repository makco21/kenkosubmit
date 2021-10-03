from logging import log
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def test():
    print('test')

def job():
    option = webdriver.ChromeOptions()
    option.binary_location = "C:\\python\\makco\\chromedriver.exe" 

    driver = webdriver.Chrome()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSejoWNAXs-b0fHj43A-3uUnjbGO8kRpgLrh-_hXQwDixXXUIQ/viewform")

    # name
    element = driver.find_element_by_xpath("//input[@class='quantumWizTextinputPaperinputInput exportInput']")
    time.sleep(5)
    element.clear()
    element.send_keys("石渠")

    # 
    element = driver.find_element_by_xpath("//div[@id='i9']")    #i9　テレワーク
    # element = driver.find_element_by_xpath("//div[@id='i12']") #出社（現場）
    element.click()

    element = driver.find_element_by_xpath("//div[@id='i22']") # 異常なし
    element.click()

    element = driver.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']")
    element.click()
    
    
    msg='今日の報告完了しました。'
    
    
    print(msg)


# job()

schedule.every().day.at("08:36").do(job)
while(True):
    schedule.run_pending()
    time.sleep(29)

