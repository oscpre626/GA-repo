#!/usr/bin/env python

import os
import time
import sys
import signal

import VL53L1X

MAX_DISTANCE_MM = 800  # Distance at which our bar is full
TRIGGER_DISTANCE_MM = 80
BAR_CHAR = u'\u2588'   # Unicode FULL BLOCK

ANSI_COLOR_RED = "\x1b[31m"
ANSI_COLOR_RESET = "\x1b[0m"

print("""trigger.py

Display a bar graph that ranges up to 80cm and turns red when it passes a trigger threshold.

Press Ctrl+C to exit.

""")


"""
Grab the width/height of the terminal using `stty size`
"""
rows, cols = [int(c) for c in os.popen("stty size", "r").read().split()]


"""
Open and start the VL53L1X ranging sensors
"""
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)  # First sensor at default address
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x2A)  # Second sensor at a different address
tof1.open()           # Initialise the i2c bus and configure the first sensor
tof1.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

tof2.open()           # Initialise the second sensor
tof2.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range


sys.stdout.write("\n")

trigger_mark = int((cols / float(MAX_DISTANCE_MM)) * TRIGGER_DISTANCE_MM)

sys.stdout.write("|".rjust(trigger_mark + 7, " ") + " - {:04.1f}cm ".format(TRIGGER_DISTANCE_MM / 10.0) + "\n")

running = True


def exit_handler(signal, frame):
    global running
    running = False
    tof1.stop_ranging()
    tof2.stop_ranging()
    sys.stdout.write("\n")
    sys.exit(0)


signal.signal(signal.SIGINT, exit_handler)

while running:
    distance_in_mm_1 = tof1.get_distance()  # Get distance from sensor 1
    distance_in_mm_2 = tof2.get_distance()  # Get distance from sensor 2

    distance_in_mm_1 = min(MAX_DISTANCE_MM, distance_in_mm_1)  # Cap at MAX_DISTANCE
    distance_in_mm_2 = min(MAX_DISTANCE_MM, distance_in_mm_2)  # Cap at MAX_DISTANCE

    bar_size_1 = int((distance_in_mm_1 / float(MAX_DISTANCE_MM)) * (cols // 2 - 10))  # Scale bar for sensor 1
    bar_size_2 = int((distance_in_mm_2 / float(MAX_DISTANCE_MM)) * (cols // 2 - 10))  # Scale bar for sensor 2

    bar_1 = BAR_CHAR * bar_size_1  # Create bar for sensor 1
    bar_2 = BAR_CHAR * bar_size_2  # Create bar for sensor 2

    # Pad the bars to full width
    bar_1 = bar_1.ljust(cols // 2 - 7, u' ')
    bar_2 = bar_2.ljust(cols // 2 - 7, u' ')

    sys.stdout.write("\r")  # Return the cursor to the beginning of the current line
    if distance_in_mm_1 < TRIGGER_DISTANCE_MM:
        sys.stdout.write(ANSI_COLOR_RED)
    sys.stdout.write(u"{:04.1f}cm {}".format(distance_in_mm_1 / 10.0, bar_1))  # Output sensor 1 data
    sys.stdout.write(ANSI_COLOR_RESET)

    if distance_in_mm_2 < TRIGGER_DISTANCE_MM:
        sys.stdout.write(ANSI_COLOR_RED)
    sys.stdout.write(u"{:04.1f}cm {}".format(distance_in_mm_2 / 10.0, bar_2))  # Output sensor 2 data
    sys.stdout.write(ANSI_COLOR_RESET)

    sys.stdout.flush()  # Flush the output buffer
    time.sleep(0.1)
