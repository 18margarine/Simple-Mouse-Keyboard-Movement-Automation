This function provides three simple automation methods that allow users to interact with their system programmatically. It is designed for tasks such as GUI automation, repetitive workflows, and script-based control.
1. Image Recognition Automation
  The function can search the user’s screen for a specific image and automatically click it once a match is found.
  Uses image recognition to locate UI elements visually
  Ideal when element positions vary
  Clicks the matched region with adjustable confidence levels
2. Coordinate-Based Automation
  Alternatively, the function can directly move the mouse to predefined screen coordinates and perform a click.
  Fast and lightweight
  Suitable for fixed-position buttons, icons, or UI regions
  Requires only X/Y values to execute
3. Input Recording & Playback
  The function can record both mouse movements/clicks and keyboard input, then export this data as a CSV file. This file can later be used with replay_movement.py to reproduce the recorded actions.
  Captures real user interactions
  Saves timestamps, positions, and keys pressed
  Playback accurately simulates the original behavior
