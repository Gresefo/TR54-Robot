class basicOnePointComponent:
    """Gives the speed the robot needs to go"""
    
    def __init__(self,acceleration,max_speed):
        """
        Constructor
        :param acceleration: int the value at which the robot accelerate
        :param max_speed: the maximum speed the robot can go
        """
        self._acceleration = acceleration
        self._max_speed = max_speed
        
    def compute(self, error, deltatime):
        """
        Return the speed to go
        :param error: the error
        :param deltatime: the delta time
        """
        speed = max(min(self._max_speed,self._acceleration*(error)),0)
        return speed