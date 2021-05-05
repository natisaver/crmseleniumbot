from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Users\user\Downloads\chromedriver.exe" 
# chrome driver exe location, add r to indicate path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get('https://inscrm-uat.successit.net/AllInsCRM/#/Login')

# driver = webdriver.Chrome(PATH)
# driver.get("https://inscrm-uat.successit.net/AllInsCRM/#/Login")
# login
username = driver.find_element_by_xpath('//*[@id="ng-app"]/app-root/app-page-outlet/app-page-login/div/main/div/div/div/div/div[2]/div/div/form/div/div[1]/div/div[1]/div/wm-input/input')
username.send_keys("admin@uat.com")
password = driver.find_element_by_xpath('//*[@id="ng-app"]/app-root/app-page-outlet/app-page-login/div/main/div/div/div/div/div[2]/div/div/form/div/div[1]/div/div[2]/div/wm-input/input')
password.send_keys("Success!23")
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((find_element_by_name('loginButton'), "loginButton"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "loginButton"))).click()
# click quotation
driver.get('https://inscrm-uat.successit.net/AllInsCRM/#/Quotation_List_v1')
driver.find_elements_by_class_name('btn app-button dropdown-toggle btn-primary')

# driver.find_element_by_anchor('//*[@id="ng-app"]/app-root/app-page-outlet/app-page-dashboard/div/main/div/aside/app-partial-leftnav/section/ul/li[2]/a[2]/span[2]')
# driver.find_element_by_css_selector("a[name='QuotationLink_SinglePage']").click()
driver.find_element_by_xpath('//*[@id="ng-app"]/app-root/app-page-outlet/app-page-quotation_list_v1/div/main/div/div/div[2]/div[1]/div/div/div[3]/div[3]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="ng-app"]/app-root/app-page-outlet/app-page-quotation_list_v1/div/main/div/div/div[2]/div[1]/div/div/div[3]/div[3]/div/div[3]/ul/li[2]/a').click()