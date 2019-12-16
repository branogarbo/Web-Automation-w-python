import pyautogui as gui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep,time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://galacticinn.netlify.com')
gui.moveTo(2223,142,1)
gui.click()
gui.press('f11')

sleep(1)

roominputs = browser.find_elements_by_css_selector('.room > input')

for i in range(2):
  for roominp in roominputs:
    roominp.send_keys('this is selenium,two,three,four',Keys.ENTER)
    sleep(0.2)

  for roominp in roominputs:
    roominp.send_keys('1,2,3,4',Keys.ENTER)
    sleep(0.2)

roombuttons = browser.find_elements_by_css_selector('.room > button')

# for roombutt in roombuttons and i in range(3):   doesnt work
#   roombutt.click()

for i in range(3):
  for roombutt in roombuttons:
    roombutt.click()