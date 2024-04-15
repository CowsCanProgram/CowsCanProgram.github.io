import pyautogui
import time
# Example: Hold down the 'a' key for 3 seconds
try:
    time.sleep(5)
    pyautogui.keyDown('option')
    for i in range(0, 15, 1):
        pyautogui.keyDown('a')
        time.sleep(48.5)
        pyautogui.keyUp('a')
        pyautogui.keyDown('s')
        time.sleep(48.7)
        pyautogui.keyUp('s')
    pyautogui.keyUp('option')
    pyautogui.press('/')
    pyautogui.press('w')
    pyautogui.press('a')
    pyautogui.press('r')
    pyautogui.press('p')
    pyautogui.press('space')
    pyautogui.press('g')
    pyautogui.press('a')
    pyautogui.press('r')
    pyautogui.press('d')
    pyautogui.press('e')
    pyautogui.press('n')
    pyautogui.press('return')
except KeyboardInterrupt:
    print('Done')
        