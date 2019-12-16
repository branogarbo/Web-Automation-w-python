import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://galacticinn.netlify.com')
pyautogui.moveTo(2223,142,1)
pyautogui.click()
browser.refresh()

sleep(1)

roominputs = browser.find_elements_by_css_selector('.room > input')

for roominp in roominputs:
  roominp.send_keys('this is selenium,two,three,four',Keys.ENTER)
  sleep(0.2)