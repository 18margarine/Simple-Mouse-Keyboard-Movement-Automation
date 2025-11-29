import pyautogui
import time

scan_region = (0,0,1920,120)

def locate_image(image, region=None):
    try:
        # Added optional region to scan only a portion of the screen
        if region is not None:
            found = pyautogui.locateOnScreen(image, region=region, confidence=0.9)
        else:
            found = pyautogui.locateOnScreen(image, confidence=0.9)
        pyautogui.click(found)
        print(f"{image} - Image found")
        time.sleep(.5)
        return True
    except pyautogui.ImageNotFoundException:
        print(f"{image} - Image Not Found")
        return False

def locate_site(image2, site_region=None):
    if site_region is not None:
        if not locate_image(image2, site_region):
            locate_image('new tab.png',site_region)
            locate_image(image2, site_region)
    else:
        if not locate_image(image2):
            locate_image('new tab.png')
            locate_image(image2)
time.sleep(1)
# Locate firefox
if locate_image('firefox.png'):
    # Locate sites in firefox, open new tab if not found
    locate_site('twitch.png', scan_region)
    locate_site('youtube.png', scan_region)
# Locate chrome
locate_image('chrome.png')


