#! python3
# looking_busy.py - will slightly nudge the cursor to prevent from looking idle
"""
Many instant messaging programs determine whether you are idle, or away from your
computer, by detecting a lack of mouse movement over some period of time—say,
ten minutes. Maybe you’d like to sneak away from your desk for a while but don’t
want others to see your instant messenger status go into idle mode. Write a script
to nudge your mouse cursor slightly every ten seconds. The nudge should be small
enough so that it won’t get in the way if you do happen to need to use your computer
 while the script is running.
"""
import pyautogui
import random
import time


# While not needed, I think creating a list of random movements is the best way
# for this program. If you are gone for a long period of time, there is a very high
# chance your mouse will not run to the edge of the screen. However, you can
# choose not to use random movements and just do one instead if you prefer.
random_movements = [
    (1, 1),
    (1, -2),
    (-1, 1),
    (-1, -1)
]
# time.sleep(10) seconds will allow it to randomly move every 10 secons until
# the user ends the program themselves. Like with random_chores.py, use
# random.choice from the random_movements list to move the mouse
try:
    while True:
        time.sleep(10)
        pyautogui.moveRel(random.choice(random_movements))
except pyautogui.FailSafeException:
    print('Program finished.')
