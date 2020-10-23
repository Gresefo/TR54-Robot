from pybricks.ev3devices import Motor
from pybricks.parameters import Port

class RobotState:
    def __init__(self):
        self.maxSpeed = 200 #mm
        self.maxdist = 2 #meters
        self.speed = 360
        self.turnDiameter = 186 #mm
        self.wheelDiameter=35 #mm
        
        self.motor_left = Motor(Port.B)
        self.motor_right = Motor(Port.C)

        self.dist = 0
        self.color = [0,0,0]
    
    def follow_start(self) : 
        return
