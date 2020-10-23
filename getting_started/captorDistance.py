import sys

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.tools import wait

class captorDistance:
    def __init__(self):
        self.infraredSensor = InfraredSensor(Port.S2)
        
    def getDistance(self):
        dMesurer = self.infraredSensor.distance()
        #distance = dMesurer**2*0.0177 + dMesurer*0.0167 + 7.7471
        distance = dMesurer*1.0356 - 4.3746
        #print(distance)

        return distance