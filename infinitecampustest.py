from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://hawaii.infinitecampus.org/campus/portal/students/hawaii.jsp')
usernameInp = browser.find_element_by_css_selector('#username')
passwordInp = browser.find_element_by_css_selector('#password')

usernameInp.send_keys('4540900574')
passwordInp.send_keys('4540900574bl',Keys.ENTER)

browser.get('https://hawaii.infinitecampus.org/campus/nav-wrapper/student/portal/student/grades')

sleep(20)

browser.execute_script('document.querySelector("body > app-root > ng-component > app-grades > app-portal-page > div.toolbar").style = "background:red;"') #aint workin doe