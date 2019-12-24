import pyautogui as gui
from time import sleep

sleep(1)

it = 0+1+1+1

print(f'edit {it}')

sleep(1)

gui.hotkey('ctrl','win','down')
gui.moveTo(566,282,0.5)
gui.click()
gui.typewrite('+1')

gui.hotkey('ctrl','s')

gui.moveTo(1080,1472,0.5)
gui.click()

sleep(0.5)

gui.typewrite('py Documents\GitHub\Web-Automation-w-python\selfeditingprogram.py')
gui.hotkey('enter')