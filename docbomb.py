from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time,sleep

browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Dmkt_docs&followup=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Dmkt_docs&ltmpl=docs&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

emailinp = browser.find_element_by_css_selector('#identifierId')
emailinp.send_keys('brianl.ext@gmail.com',Keys.ENTER)

sleep(1)

passinp = browser.find_element_by_name('password')
passinp.send_keys('roughrider22',Keys.ENTER)