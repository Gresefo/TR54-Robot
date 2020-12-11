from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

class twoWheelsController:

    def __init__(self, left_motor_output, right_motor_output, min_steering, max_steering, min_speed, max_speed, wheelDiameter, axeDiameter):
        """
        Initializes a controller with two wheels.
        :param left_motor_output: the output pin for the left motor
        :param right_motor_output: the output pin for the right motor
        :param min_steering: the minimum steering in [-100; 100]
        :param max_steering: the maximum steering in [-100; 100]
        :param min_speed: the minimum speed in [-100; 100]
        :param max_speed: the maximum speed in [-100; 100]
        """
        self._max_steering = max_steering
        self._min_steering = min_steering
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._motor_left = Motor(left_motor_output)
        self._motor_right = Motor(right_motor_output)
        self._drive_base = DriveBase(self._motor_left,self._motor_right,wheelDiameter,axeDiameter)

    def drive(self, steering, speed):
        """
        Drives using the given steering and speed limited to defined bounds.
        :param steering: the steering to apply in [-100; 100]
        :param speed: the speed to apply in [-100; 100]
        """
        apply_steering = min(self._max_steering, max(self._min_steering, steering))
        apply_speed = min(self._max_speed, max(self._min_speed, speed))
        self._drive_base.drive(apply_speed,apply_steering)

    def stop(self):
        """ Stops moving. """
        self._drive_base.drive(0,0)