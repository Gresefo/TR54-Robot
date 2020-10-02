#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port


from pybricks.tools import wait
import sys

from motorControl import motorControl 

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
print(sys.version)

#ev3.speaker.beep(5)



# Initialize a motor at port B.
    #motor_left = Motor(Port.B)
    #motor_right = Motor(Port.C)

mc = motorControl()
ev3.speaker.beep(30)
mc.forward(mc.speed)
wait(3000)
mc.stop()
wait(1000)
mc.rotate_right()
wait(1000)
mc.rotate_right(120)
wait(1000)
ev3.speaker.beep(30)
