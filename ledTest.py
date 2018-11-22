#!/usr/bin/python
import time
import RPi.GPIO as io

io.setmode(io.BCM)

led = 19
lane1 = 24
lane2 = 25
lane3 = 26

io.setup(led, io.OUT)
io.setup(lane1, io.IN, pull_up_down=io.PUD_UP)
io.setup(lane2, io.IN, pull_up_down=io.PUD_UP)
io.setup(lane3, io.IN, pull_up_down=io.PUD_UP)

io.output(led, io.LOW)

while True:

    if io.input(lane1) == False or io.input(lane2) == False or io.input(lane3) == False:
        io.output(led, io.LOW)

#    elif KeyboardInterrupt:
#        break
#        io.cleanup()

    else:
        io.output(led, io.HIGH)

io.cleanup()
