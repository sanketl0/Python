import pyautogui
import  time


time.sleep(3)
count = 0
while count <= 2000:
    pyautogui.typewrite("")
    pyautogui.press("enter")
    count = count +1


