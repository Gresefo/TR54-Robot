from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor


class twoWheelsController:

    def __init__(self, left_motor_output, right_motor_output, min_steering, max_steering, min_speed, max_speed, wheelDiameter, axeDiameter, steering_treshold=12,prev_steering_size=10):
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

        #internal variable to determine wich segment the robot is on currently
        #self.prev_steering = numpy.zeros(shape = (20))
        self.prev_steering = [0]*prev_steering_size
        self.prev_angle = [0]*10
        self.action = 0
        self.steering_treshold = steering_treshold
        self.current_action = ['going_straight','turning_right','turning_left']
        self.current_angle = 0


    def drive(self, steering, speed):
        """
        Drives using the given steering and speed limited to defined bounds.
        :param steering: the steering to apply in [-100; 100]
        :param speed: the speed to apply in [-100; 100]
        """
        apply_steering = min(self._max_steering, max(self._min_steering, steering))
        apply_speed = min(self._max_speed, max(self._min_speed, speed))
        #self.prev_steering = np.append([apply_steering], self.prev_steering[0:-1])
        self.prev_steering.pop(0)
        self.prev_steering.append(apply_steering)
        #self.update_action()

        self.prev_angle.pop(0)
        self.prev_angle.append(self.getAngle())
        #print(self.prev_angle)
        self.update_angle()
        self.update_action()
        

        self._drive_base.drive(apply_speed,apply_steering)

    def stop(self):
        """ Stops moving. """
        self._drive_base.drive(0,0)

    def update_action(self):
        #steering_mean = numpy.mean(self.prev_steering)
        steering_mean = sum(self.prev_steering)/len(self.prev_steering)

        if steering_mean>self.steering_treshold:
            if self.action != 1:
                self.action=1
                #print("controller",self.current_action[self.action])
        elif steering_mean< -self.steering_treshold:
            if self.action != 2:
                self.action=2
                #print("controller",self.current_action[self.action])
        else:
            if self.action != 0:
                self.action=0
                #print("controller",self.current_action[self.action])

    def update_angle(self):
        angle_mean = int(sum(self.prev_angle)/len(self.prev_angle))
        self.current_angle = angle_mean
        #print(self.current_angle)

    def getAngle(self):
        return self._drive_base.angle()