#!/usr/bin/python
import time
import RPi.GPIO as io
import Adafruit_CharLCD as LCD


def timeLane1(channel):
	
    endTime1 = time.time()
    print(endTime1)
    global time1
    time1 = endTime1 - startTime
    print("Lane 1 Done! \n" + str(time1))
    io.remove_event_detect(lane1)

def timeLane2(channel):
	
    endTime2 = time.time()
    print(endTime2)
    global time2
    time2 = endTime2 - startTime
    print("Lane 2 Done! \n" + str(time2))
    io.remove_event_detect(lane2)

def timeLane3(channel):
	
    endTime3 = time.time()
    print(endTime3)
    global time3
    time3 = endTime3 - startTime
    print("Lane 3 Done! \n" + str(time3))
    io.remove_event_detect(lane3)

def race():

# Let's us know function was called

    io.setmode(io.BCM)

    lcd = LCD.Adafruit_CharLCDPlate()

    global startGate
    global lane1
    global lane2
    global lane3
    startGate = 23
    lane1 = 24
    lane2 = 25
    lane3 = 26

    io.setup(startGate, io.IN, pull_up_down=io.PUD_UP)
    io.setup(lane1, io.IN, pull_up_down=io.PUD_UP)
    io.setup(lane2, io.IN, pull_up_down=io.PUD_UP)
    io.setup(lane3, io.IN, pull_up_down=io.PUD_UP)

    lcd.set_color(1.0, 1.0, 1.0)
    lcd.clear()
    lcd.message('   START YOUR \n   ENGINES!!!')
    print("Race Starting")
    time.sleep(1)

# Waiting for startGate to Rise because of Pull Up

    io.wait_for_edge(startGate, io.RISING)
    time.sleep(1)

# When startGate rises records time
    global startTime
    startTime = time.time()
    print(startTime)

# Adding interrupts for lanes
# When they are called will 
# trigger their distinct function 
   
    io.add_event_detect(lane1, io.FALLING, callback=timeLane1, bouncetime=1000)
    io.add_event_detect(lane2, io.FALLING, callback=timeLane2, bouncetime=1000)
    io.add_event_detect(lane3, io.FALLING, callback=timeLane3, bouncetime=1000)
    io.wait_for_edge(startGate, io.FALLING)
    global time1
    global time2
    global time3
    time1 = "{0:.2f}".format(time1)
    time2 = "{0:.2f}".format(time2)
    time3 = "{0:.2f}".format(time3)
    print(str(time1) + " " + str(time2) + " " + str(time3))
    lcd.clear()
    lcd.message('  L1   L2   L3   \n' + ' ' + time1 + ' ' + time2 + ' ' + time3)
#    time.sleep(15)

# When startGate is reset race is called again

# while True:

try:
        race()

except KeyboardInterrupt:
#        break
        io.cleanup()
        exit()

finally:
   io.cleanup()
