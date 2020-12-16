class basicOnePointComponent:
    
    def __init__(self,acceleration,max_speed):
        self._acceleration = acceleration
        self._max_speed = max_speed
        
    def compute(self, error, deltatime):
        
        speed = max(min(self._max_speed,self._acceleration*(error)),0)
        return speed