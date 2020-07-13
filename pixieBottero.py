from PIL import ImageGrab, ImageOps
from time import sleep
import win32gui
import pyautogui



def moveWindow():
    window = win32gui.FindWindow(None, "Nostale")
    win32gui.SetForegroundWindow(window)
    rect = win32gui.GetWindowRect(window)

    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    win32gui.MoveWindow(window, 0, 0, w, h, True)

def getPixelColor():
    screenshot = ImageGrab.grab(bbox=(445,425,500,550)) # X1,Y1,X2,Y2
    x = 21
    y = 7
    pix_up_color = screenshot.getpixel((x,y))
    pix_down_color = screenshot.getpixel((x,y+108))
    return [pix_up_color, pix_down_color]
    

def pressLeftKey():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

def pressRightKey():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

    
moveWindow()

while 1:
    [pu, pd] = getPixelColor()
    if pu[0] < 120 and pu[1] < 80 and pu[2] < 30:
        pressLeftKey()
        if pd[0] < 120 and pd[1] < 80 and pd[2] < 30:
            pressRightKey()
        sleep(0.095)
    if pd[0] < 120 and pd[1] < 80 and pd[2] < 30:
        pressRightKey()
        if pu[0] < 120 and pu[1] < 80 and pu[2] < 30:
            pressLeftKey()
        sleep(0.095)

