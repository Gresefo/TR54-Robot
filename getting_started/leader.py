import sys

from pybricks.tools import wait
from motorControl import motorControl

class leader:
    def __init__(self, Ti, state):
        self.Ti = Ti
        self.mc = motorControl(state)
        self.state = state
        self.leading(40)

    def leading(self,percentVmax):
        while(True):
            self.mc.forwardDrive(percentVmax)
            wait(self.Ti)
            self.mc.stop()
            wait(self.Ti)