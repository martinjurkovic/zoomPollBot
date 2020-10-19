import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.FAILSAFE = True

width, height = pyautogui.size()

print(width)
print(height)

while True:
    position = pyautogui.locateCenterOnScreen('slika1.png')
    if (position):
        x = position.x/2
        y = position.y/2
        x_of = 155
        y_of = -140
        print(x-x_of, y-y_of)
        pyautogui.click(x-x_of, y-y_of)
        position2 = pyautogui.locateCenterOnScreen('im5.png')
        if position2:
            x2 = position2.x/2
            y2 = position2.y/2
            x_of2 = 0
            y_of2 = 0
            print(x2-x_of2, y-y_of2)
            pyautogui.click(x2-x_of2, y2-y_of2)
        else:
            print("not2")
    else:
        print("not")    
    