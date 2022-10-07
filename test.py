# %%
import import_ipynb
import time
from matplotlib.style import available
from reload_module import reload_module
from selenium.common.exceptions import *
# import os
# from ipynb_to_py import ipynb_to_py
# ipynb_to_py(os.getcwd(),'benepia')

retry_count = 3
reload_module('global_function')
import global_function as gf

benepia = reload_module('benepia')
def benepia_scheduler(year, month, condoNm, desired_dates, roomNm='전체', auto_reservation=False):
    driver = gf.set_driver()
    url = 'https://skhynix.benepia.co.kr/ecampus/condoBookList.do' 
    bp = benepia.auto_reservation('2074661', '199829867', 'benepia')
    driver = bp.get_url(driver, url)
    # for _ in range(retry_count):
    #     try:
    #         driver = bp.check_hotel(driver, condoNm='리솜', roomNm='포레스트빌라형(S30)28평') 
    #     except NoSuchElementException:
    #         break

    driver = bp.check_hotel(driver, condoNm, roomNm) 
    time.sleep(1)

    if roomNm != '전체': # roomNm이 전체가 아닌 경우, 추가 진행
        driver = bp.select(driver, year, month, condoNm, roomNm)
        time.sleep(1)
        driver, available_dates = bp.get_available_dates(driver, year, month, condoNm, roomNm, desired_dates)
        time.sleep(1)

    if auto_reservation == True: # auto == True인 경우 추가 진행
        driver = bp.make_reservation(driver, condoNm, roomNm, available_dates, desired_dates,)

    return driver

# driver = benepia_scheduler('2022','10','리솜','포레스트빌라형(S30)28평',['20221005'], auto_reservation=False)
driver = benepia_scheduler('2022','10','리솜',['20221005'], roomNm='전체', auto_reservation=False)

# clear_logger()




# %%
# import os
# import chromedriver_autoinstaller # chromedriver auto update
# import importlib # module reload
# import time
# import schedule
# import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import *
# from webdriver_manager.chrome import ChromeDriverManager
# from global_function import create_logger
# from global_function import select_value_from_dropdown
# from global_function import set_driver, page_back, get_weekday, check_alert
# from reload_module import reload_module


