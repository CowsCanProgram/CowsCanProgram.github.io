import pyautogui
import time
# Example: Hold down the 'a' key for 3 seconds
time.sleep(5)
for i in range(0, 15, 1):
    try:
        with pyautogui.hold('option'):
            pyautogui.keyDown('a')
            time.sleep(50)
            pyautogui.keyUp('a')
        with pyautogui.hold('option'):
            pyautogui.keyDown('s')
            time.sleep(50)
            pyautogui.keyUp('s')
    except KeyboardInterrupt:
        print('Done')
        break
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

print('Done')