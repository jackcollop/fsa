from selenium import webdriver
import time
import os
import datetime
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
# Memory optimization
options.add_argument('--disk-cache-size=1')
options.add_argument('--media-cache-size=1')
options.add_argument('--incognito')
options.add_argument('--remote-debugging-port=9222')

prefs = {"download.default_directory" : os.getcwd()}
options.add_experimental_option("prefs",prefs)

service = Service('/usr/local/bin/chromedriver')
  
driver = webdriver.Chrome(service=service, options=options)
driver.execute_cdp_cmd(
    "Page.setDownloadBehavior", {"behavior": "allow", "downloadPath": os.getcwd()}
    )
driver.get('https://apps.fsa.usda.gov/sorspub/reports/web/public/loan-maturity-national')

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

select = Select(driver.find_element(by=By.ID, value='commodity'))
select.select_by_visible_text('COTTON-UP')

time.sleep(3)

driver.execute_script("javascript:submitRequest('/sorspub/reports','csv')")

time.sleep(1)

driver.get('https://apps.fsa.usda.gov/sorspub/reports/web/public/loan-maturity-state')

time.sleep(1)

select = Select(driver.find_element(by=By.ID,value='commodity'))
select.select_by_visible_text('COTTON-UP')

select = Select(driver.find_element(by=By.ID,value='cropYear'))
select.select_by_visible_text('2024')

time.sleep(1)
driver.execute_script("javascript:submitRequest('/sorspub/reports','csv')")

time.sleep(1)

driver.quit()
