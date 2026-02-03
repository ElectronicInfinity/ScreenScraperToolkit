import pyautogui
import keyboard
while True:
    keyboard.wait('i')
    x, y = pyautogui.position()
    print("Mouse at:", (x, y))
    print("RGB:", pyautogui.pixel(x, y))
