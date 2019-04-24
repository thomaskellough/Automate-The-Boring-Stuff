#! python3
# pretty_stopwatch.py - stopwatch with 'pretty' output as well as copying to clipboard

import time
import pyperclip

start_time = time.time()
last_time = start_time
lap_num = 1
lines = []
# There isn't too much to add to this program, but a few ljust and rjust methods
# and the pyperclip. The rjust and ljust can be confusing, luckily this program
# is very easy to try out with different values. Note: If you're using an IDE like
# PyCharm, they KeyboardInterrupt may not work. Try using this program in IDLE if
# that is the case.
try:
    while True:
        input()
        line = ''
        lap_time = format(round(time.time() - last_time, 2), '.2f')
        total_time = format(round(time.time() - start_time, 2), '.2f')
        lapNum = 'Lap #%s: ' % str(lap_num)
        totalTime = str(total_time).rjust(5)
        lapTime = ' (%s)' % str(lap_time).rjust(5)
        totalPrint = (lapNum + totalTime + lapTime)
        print(totalPrint, end='')
        lines.append(totalPrint)
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')

text = '\n'.join(lines)
pyperclip.copy(text)
