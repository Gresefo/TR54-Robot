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
from pybricks.iodevices import Ev3devSensor

import sys

from motorControl import motorControl 
from leader import leader
from Follower import Follower
from captorDistance import captorDistance
from RobotState import RobotState
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

state = RobotState()
follower = Follower(state)

#l = leader(1000)

# Write your program here.
print(sys.version)

#ev3.speaker.beep(5)



