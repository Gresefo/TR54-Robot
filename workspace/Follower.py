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
import csv

#from openpyxl import Workbook

from motorControl import motorControl
from captorDistance import captorDistance

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

class follower:
    def __init__(self,state) :
        self.motorControl = motorControl(state)
        self.state = state
        self.cd = captorDistance()
        #self.all_or_nothin_follow()
        #self.up_to_point_follow()
        self.two_points_follow()
        

    def all_or_nothin_follow(self) :
        while(True):
            wait(500)
            dist = self.cd.getDistance()
            if(dist >= 30):
                self.motorControl.forwardDrive(50)
            else:
                self.motorControl.stop()

            print(dist)

        return

    def up_to_point_follow(self) :
        a = 2
        d = 30
        while(True):
            wait(100)
            dist = self.cd.getDistance()
            percent = max(min(50,a*(dist-d)),0)
            self.motorControl.forwardDrive(percent)
            #self.writeEXCEL('A1')
            print(dist , ";",percent)
        return
    
    def two_points_follow(self):
        prev_v = 0
        af = 2
        aa = 5
        df = 30
        da = 50
        while(True):
            wait(100)
            dist = self.cd.getDistance()
            percentF = min(max(af*(dist-df),0),50)
            percentA = min(max(aa*(dist-da),0,prev_v),50)
            percent = min(percentA,percentF)
            self.motorControl.forwardDrive(percent)
            prev_v = percent
            print(dist , ";",percent)
        return

    def writeEXCEL(self,cell):
        wb = Workbook()
        # grab the active worksheet
        ws = wb.active
        # Data can be assigned directly to cells
        ws[cell] = 4
        # Rows can also be appended
        # Python types will automatically be converted
        #import datetime
        #ws['A2'] = datetime.datetime.now()
        # Save the file
        wb.save("sample.xlsx")

