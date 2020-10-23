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

from pybricks.robotics import DriveBase

import math


from pybricks.tools import wait
from RobotState import RobotState
import sys

class motorControl:
    def __init__(self,state):
        """
            Constructor
        """       
        self.motor_left = Motor(Port.B)
        self.motor_right = Motor(Port.C)
        self.state = state
        self.db = DriveBase(self.motor_left,self.motor_right,self.state.wheelDiameter,self.state.turnDiameter)
        

    def forward(self,*params):
        if(len(params)>0):
            if(params[0]>=0 and params[0]<=100):
                 
                speed = self.state.maxspeed * params[0]/100
                self.motor_left.run(speed)
            else:
                print("error,param too big")
        else :
            self.motor_right.run(self.state.speed)
        
        return
    
    def forwardPercent(self,percent):
        self.motor_left.dc(percent)
        self.motor_right.dc(percent)

        return

    def forwardDrive(self,percent):
        speed = self.state.maxSpeed * percent / 100
        self.db.drive(speed,0)
        return

    def rotate_right (self,*speed):
        #360 , 10 = 15/8 tours
        print("entered rotate")
        if(len(speed)>=1):
            self.stop()
            self.motor_left.run(-speed[0])
            self.motor_right.run(speed[0])
        else:
            self.stop()
            self.motor_left.run(self.speed)
            self.motor_right.run(-self.speed)
        wait(10000)
        self.stop()
        return

    def rotate_left (self,*speed):
        if(len(speed)>=1):
            self.stop()
            self.motor_left.run(-speed[0])
            self.motor_right.run(speed[0])
        else:
            self.stop()
            self.motor_left.run(-self.speed)
            self.motor_right.run(self.speed)
        wait(10000)
        self.stop()
        return


    
    def rotate (self, angle, *params):
        """
            Rotate the robot on himself to a given angle with a rotation speed of 360

            :param angle: the rotation angle, left turn is positiv, right turn is negativ
        """

        if(len(params) > 1):
            print('Too many parameters, enter just an angle and a time (s)')
        else:
            # Time not in parameter
            if(len(params) == 0):
                time = abs(angle) * math.pi * self.state.turnDiameter /(self.state.wheelDiameter * math.pi * self.state.speed)
                time = time * 1000
                speed = self.state.speed
            # Time is in parameter
            else:
                time = params[0]
                speed = (int)(abs(angle) * math.pi * self.state.turnDiameter /(self.state.wheelDiameter * math.pi * time))
                print(speed)
                print(time)


            if(angle>=0):
                turnLeft = 1
            else :
                turnLeft = -1
            
            # Execution
            self.stop()
            self.motor_left.run(-1*turnLeft*speed)
            self.motor_right.run(turnLeft*speed)
            wait(time)

        self.stop()
        return
        



    def stop(self):
        self.db.stop()
        return

