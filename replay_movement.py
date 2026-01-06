import pyautogui
import pandas as pd
from prompt import CSVBrowse, TextBrowse
import time
'''
This is a simple automated form or data entry script or any repetitive menial tasks.
'''
# Prompt window will be shown to search for a text file that will be used for autofill a form
try:
    text_browse = TextBrowse()
    text_browse.mainloop()
    text_path = text_browse.filename
    # Prompt window will be shown to search for csv generated from record_movement.py
    csv_browse = CSVBrowse()
    csv_browse.mainloop()
    csv_path = csv_browse.filename

    # This is just a sample text that will replace the keystroke from record_movement.py
    with open(text_path) as f:
        listed_info = tuple(item.strip() for item in f)

    text_sample = [listed_info]
    df = pd.read_csv(csv_path, header=None)
    pyautogui.MINIMUM_DURATION = 0.01
    # Calibrate the value for fine-tuning of scroll
    SCROLL_PER_TICK = 120
    # Iterate on each item in list
    for item in text_sample:
        text_iter = 0
        # Iterate on coordinates recorded
        for index, rows in df.iterrows():
            if rows[0] == 'move':
                pyautogui.moveTo(x=int(rows[1]), y=int(rows[2]))
                if float(rows[3]) > 1.00:
                    time.sleep(float(rows[3]))
            elif rows[0] == 'click':
                pyautogui.click(x=int(rows[1]), y=int(rows[2]))
            elif rows[0] == 'key':
                pyautogui.write(item[text_iter])
                time.sleep(1)
                text_iter += 1
            elif rows[0] == 'scroll':
                pyautogui.scroll(int(rows[2]) * SCROLL_PER_TICK)
            elif rows[0] == 'enter':
                pyautogui.press('enter')

except (FileNotFoundError, ValueError, TypeError) as e:
    print("Automation Cancelled")

