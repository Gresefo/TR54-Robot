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

class motorControl:
    def __init__(self):
        self.speed = 360
        
        self.motor_left = Motor(Port.B)
        self.motor_right = Motor(Port.C)

    def forward(self,speed):
        self.motor_left.run(self.speed)
        self.motor_right.run(self.speed)
        
        return

    def rotate_right (self,*speed):
        if(len(speed)>=1):
            self.stop()
            self.motor_left.run(-speed[0])
            self.motor_right.run(speed[0])
        else:
            self.stop()
            self.motor_left.run(-480)
            self.motor_right.run(480)
        wait(2000)
        self.stop()
        return

    def rotate_left (self,*speed):
        if(len(speed)>=1):
            self.stop()
            self.motor_left.run(-speed[0])
            self.motor_right.run(speed[0])
        else:
            self.stop()
            self.motor_left.run(-480)
            self.motor_right.run(480)
        wait(2000)
        self.stop()
        return

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()
        return

