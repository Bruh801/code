import pyautogui
import time

time.sleep(5)

for i in range(10):
    pyautogui.typewrite('Hello World!')
    pyautogui.press('enter')
    time.sleep(1)
