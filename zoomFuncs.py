# from pyautogui import *
# import pyautogui
# import time
# import keyboard
# import random
# import win32api, win32con
import os
import time
import pyautogui
import win32gui
import re
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


# Controls the open windows
class WindowMgr:

    def __init__(self, wildcard):
        self.wildcard = wildcard
        self._handle = None
        self.findWindow()
        self.setForeground()

    def enumCallback(self, hwnd, wildcard):
        # Checks all open windows
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def findWindow(self):
        # Looks for desired window
        self._handle = None
        win32gui.EnumWindows(self.enumCallback, self.wildcard)

    def setForeground(self):
        # Puts the desired window into the foreground
        win32gui.SetForegroundWindow(self._handle)


def leaveMeeting():
    try:
        WindowMgr('Zoom Meeting')
        # Looks for the first leave button and clicks it
        time.sleep(2)
        while pyautogui.locateOnScreen('leave1.png', confidence=0.7) is None:
            time.sleep(0.01)
            pyautogui.press('alt')
        leaveButton = list(pyautogui.locateOnScreen('leave1.png'))
        leaveButton[0] -= 1920
        pyautogui.moveTo(leaveButton)
        pyautogui.click()

        # Clicks the second leave button to confirm
        while pyautogui.locateOnScreen('leave2.png', confidence=0.7) is None:
            time.sleep(0.01)
        leaveButton2 = list(pyautogui.locateOnScreen('leave2.png'))
        leaveButton2[0] -= 1920
        pyautogui.moveTo(leaveButton2)
        pyautogui.click()

        os.system("TASKKILL /F /IM Zoom.exe")
    except:
        print("No window is open.")


def joinMeeting(meetCode, meetPass):
    try:
        # Starts the Zoom application
        os.startfile(r"PATH-TO-ZOOM-EXECUTABLE")

        # Looks for the join meeting button and presses it once it's visible
        while pyautogui.locateOnScreen('join.png', confidence=0.9) is None:
            time.sleep(0.01)
        joinButton = list(pyautogui.locateOnScreen('join.png'))
        joinButton[0] -= 1920
        pyautogui.moveTo(joinButton)
        pyautogui.click()

        # Waits for the code input window and inputs the meeting code
        while pyautogui.locateOnScreen('inputCode.png', confidence=0.7) is None and pyautogui.locateOnScreen(
                'blockedCode.png', confidence=0.7) is None:
            time.sleep(0.01)
        pyautogui.write(meetCode)

        # Turns off the video if the box is not already checked
        while pyautogui.locateOnScreen('videooff.png') is None:
            time.sleep(0.01)
        videoOff = list(pyautogui.locateOnScreen('videooff.png'))
        videoOff[0] -= 1920
        pyautogui.moveTo(videoOff)
        pyautogui.click()

        # Locates the second join button and clicks it
        while pyautogui.locateOnScreen('join2.png') is None:
            time.sleep(0.01)
        join2Button = list(pyautogui.locateOnScreen('join2.png'))
        join2Button[0] -= 1920
        pyautogui.moveTo(join2Button)
        pyautogui.click()

        # Waits for the password input window and inputs the password followed by 'enter'
        while pyautogui.locateOnScreen('passBox.png') is None:
            time.sleep(0.01)
        pyautogui.write(meetPass)
        pyautogui.press('enter')
    except:
        print("Could not join the meeting")

