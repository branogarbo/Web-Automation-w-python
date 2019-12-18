import pyautogui as gui
from time import sleep

sleep(1)

it = 1

print(f'edit {it-1}')

sleep(1)

gui.hotkey('ctrl','winleft','down')
gui.moveTo(566,282,0.5)
gui.click()
gui.typewrite('+1')

gui.hotkey('ctrl','s')

gui.moveTo(1067,1473,0.5)
gui.click()

sleep(0.5)

gui.typewrite('py Documents\GitHub\Web-Automation-w-python\selfeditingprogram.py')
gui.hotkey('enter')