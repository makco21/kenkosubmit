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

    element = driver.find_element_by_xpath("//input[@class='quantumWizTextinputPaperinputInput exportInput']")
    time.sleep(5)
    element.clear()
    element.send_keys("石渠")

    element = driver.find_element_by_xpath("//div[@id='i12']")
    element.click()

    element = driver.find_element_by_xpath("//div[@id='i22']")
    element.click()

    element = driver.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']")
    element.click()
    
    
    msg='今日の報告完了しました。'
    
    
    print(msg)

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    
def sendEmail(msg):
    msg = MIMEText(msg, 'plain', 'utf-8')

    # 输入Email地址和口令:
    from_addr = 'sqmakco@gmail.com'
    password = 'Qsq98899889'
    # 输入收件人地址:
    to_addr = 'gztr950819@live.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.gmail.com'

    msg['From'] = _format_addr('makco <%s>' % from_addr)
    msg['To'] = _format_addr('石<%s>' % to_addr)
    msg['Subject'] = Header('体調管理報告完了', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.connect() # 追加
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()



# sendEmail('報告完了')
schedule.every().day.at("08:36").do(job)
while(True):
    schedule.run_pending()
    time.sleep(29)

