import pyautogui
import pandas as pd
from prompt import FileBrowse
'''
This is a simple automated form or data entry script or any repetitive menial tasks.
'''
# Prompt window will be shown to search for csv generated from record_movement.py
file_browse = FileBrowse()
file_browse.mainloop()
file_path = file_browse.filename

# This is just a sample text that will replace the keystroke from record_movement.py
text_sample = [('first item', 'second item')]
df = pd.read_csv(file_path, header=None)
pyautogui.MINIMUM_DURATION = 0.01
# Iterate on each item in list
for item in text_sample:
    text_iter = 0
    # Iterate on each word in tuple
    for index, rows in df.iterrows():
        if rows[0] == 'move':
            pyautogui.moveTo(x=int(rows[1]),y=int(rows[2]))
        elif rows[0] == 'click':
            pyautogui.click(x=int(rows[1]),y=int(rows[2]))
        elif rows[0] == 'key':
            pyautogui.write(item[text_iter])
            text_iter +=1
