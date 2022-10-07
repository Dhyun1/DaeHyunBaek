import os
import subprocess
import datetime
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# 파일마다 로그 생성
def create_logger(instanceNm): # instanceNm : 실행 중인 *.py의 파일명
    logger = logging.getLogger(instanceNm)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(r'%(asctime)s-%(levelname)s-[%(filename)s:%(lineno)d] %(message)s',
                                r'%Y:%m:%d, %H:%M:%S')
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)
    logFileName = datetime.datetime.now().strftime("./log/{}-%Y%m%d.log").format(instanceNm)
    fileHandler = logging.FileHandler(filename=logFileName, encoding='utf-8')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    # logger.addHandler(streamHandler)
    return logger

# driver 구동
def set_driver(implicitly_wait=3):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920x1080") # 'headless','disable-gpu','disable-infobars','--disable-extensions'
        options.add_argument("--disable-software-rasterizer")
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # 'Failed to read descriptor from node connection' 방지 옵션
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(implicitly_wait) # implicitly wait
        return driver
    except Exception as e:
        raise(Exception(e))


# page back 
def page_back(driver):
    driver.execute_script("window.history.go(-1)")
    return

# 요일 확인
def get_weekday(year,month,day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        days = ['월','화','수','목','금','토','일']
        weekday = datetime.date(year,month,day).weekday()
        return days[weekday] 
    except Exception as e:
        print(Exception(e))

## alert 확인
def check_alert(logger, driver, wait_time=3): 
    try:
        WebDriverWait(driver, wait_time).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        logger.info(f'ALERT: {alert.text}')
        return driver, alert

    except NoAlertPresentException:
        # logger.info('no alert')
        return driver, None

    except TimeoutException:
        # logger.info('no alert')
        return driver, None

    except Exception as e:
        logger.error(f'{Exception(e)}')
        return driver, None


## dropdown option 선택 (text 기준)
def select_value_from_dropdown(logger, element, text):
    select = Select(element)
    not_in_dropdown = True
    for ele in select.options:
        if (text in ele.text): # text 일부만 들어가도 조회 가능
            ele.click()
            not_in_dropdown = False
            break
    if not_in_dropdown:
        logger.error('No match found among dropdown options.')
    
    return
        




## ipynb 파일 이름 변수로 가져오기
#  from IPython.display import display,Javascript
# IPython.notebook.kernel.execute('notebookName = '${window.document.getElementById("notebook_name").innerHTML}');
# import ipyparams
# def get_nb_name():
#     nb_name = ipyparams.notebook_name
#     return nb_name
# get_nb_name()

## 서버 시간 check
# import requests
# x = requests.get('https://time.navyism.com/?host=skhynix.benepia.co.kr')
# print(x.content.decode())


## NTP 서버 동기화
# import ntplib 
# from time import ctime 
# timeServer = 'http://www.bora.net' # NTP Server Domain Or IP 
# # timeServer = '210.120.246.16'
# c = ntplib.NTPClient() 
# response = c.request(timeServer, version=3) 
# print(f'NTP server Time: {ctime(response.tx_time)}')
# print(f'NTP Server Time과 Local Time과 차이: {response.offset}s')