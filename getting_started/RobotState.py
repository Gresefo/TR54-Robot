from pybricks.ev3devices import Motor
from pybricks.parameters import Port

from pybricks.tools import DataLog, StopWatch, wait
class RobotState:
    def __init__(self,logger_desc,nb_calibrage_classe):
        self.maxSpeed = 200 #mm
        self.maxdist = 2 #meters
        self.speed = 360
        self.turnDiameter = 186 #mm
        self.wheelDiameter=35 #mm
        
        self.motor_left = Motor(Port.B)
        self.motor_right = Motor(Port.C)

        self.dist = 0
        self.color = [0,0,0]





        self.logger = DataLog("Dist","Vitesse",name="log_test_"+logger_desc,timestamp=True,extension='txt',append=False)
    
    def follow_start(self) : 
        return
