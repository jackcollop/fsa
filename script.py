from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://apps.fsa.usda.gov/sorspub/reports/web/public/loan-maturity-national')

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

select = Select(driver.find_element(by=By.ID, value='commodity'))
select.select_by_visible_text('COTTON-UP')

time.sleep(3)

driver.execute_script("javascript:submitRequest('/sorspub/reports','csv')")

time.sleep(10)
