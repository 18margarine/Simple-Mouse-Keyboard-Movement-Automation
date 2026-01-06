import time
import pynput
import csv
from prompt import App
'''
This is a simple mouse and keyboard actions recorder which gives a csv file containing the actions
made during the run of the script. CSV file can then be used in replay_movement.py to replicate the movement.
'''
SAMPLING_INTERVAL = .0085
last_event_time = time.time()
# Store mouse coordinates and key inputs in a list tuple format
action_order = [('action', 'x', 'y', 'delay')]

def current_coord (x,y):
    global last_event_time
    current_time = time.time()
    # Limit the sampling interval of mouse movement for faster mouse movement
    delta = current_time - last_event_time
    if current_time - last_event_time > SAMPLING_INTERVAL:
    # Will print the current coordinates of the mouse based on its location in the screen
        print(f"Currently at: {(x,y)}")
        action_order.append(('move', x, y, delta))
    last_event_time = current_time

# Will print current coordinates of mouse when clicked
def clicked_coord(x,y,button, pressed):
    if pressed:
        print(f"Pressed at {(x, y)} with {button}")
        action_order.append(('click', x, y, ''))
    else:
        print(f"Released at {(x,y)} with {button}")

def on_scroll(x, y, dx, dy):
    print(f'Scrolled at ({x}, {y})({dx}, {dy})')
    action_order.append(('scroll', '', dy, ''))
    if dy < 0:
        print('Scrolling down')
    elif dy > 0:
        print('Scrolling up')

# Will print what key is pressed and released (press only one key just to mark it)
# All full text will be added in replay_movement.py
def press_key(key):
    try:
        print(f"Button pressed: {key}")
        if key == pynput.keyboard.Key.enter:
            action_order.append(('enter', '', '', ''))
        else:
            action_order.append(('key','','', ''))
    except AttributeError:
        print(f"Special key pressed: {key}")
# Will end mouse and keyboard recording
def release_key(key):
    print(f"{key} released.")
    if key == pynput.keyboard.Key.esc:
        mouse_listen.stop()
        keyboard_listen.stop()

mouse_listen = pynput.mouse.Listener (on_move=current_coord, on_click=clicked_coord, on_scroll=on_scroll)
keyboard_listen = pynput.keyboard.Listener(on_press=press_key, on_release=release_key)
mouse_listen.start()
keyboard_listen.start()

keyboard_listen.join()
mouse_listen.join()

# Delete last key pressed which is 'Esc'
del action_order[-1]
# Will prompt the user to enter filename for the csv
window = App()
window.mainloop()
f_name = window.stored_file_name
# Save all coordinates movements and keystrokes to csv
with open(f'{f_name}.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(action_order)