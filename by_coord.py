import pyautogui
import time
import sys
# COORDINATES OF ITEMS TO CLICK ON SCREEN
firefox = (174,1069)
twitch = (469, 97)
pycharm = (317, 1066)
youtube = (545,99)
chrome = (204,1065)

def mouse_click(coord):
    pyautogui.click(x=coord[0], y=coord[1], button='left')
    time.sleep(2)

time.sleep(3) #Add delay in seconds
user_response = pyautogui.confirm(text="Press OK to run the script or Cancel to close.",
                                  title='Confirmation', buttons=['OK','Cancel'])

if user_response == 'Cancel':
    print('Script cancelled')
    sys.exit()
else:
    mouse_click(firefox)
    mouse_click(twitch)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    mouse_click(youtube)
    mouse_click(chrome)
    mouse_click(pycharm)