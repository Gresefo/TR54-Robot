class basicDriver:
    """ Defines a driver component for driving a robot. """

    def __init__(self, steering_component, speed_component, color_sensor_component, distance_sensor_component,
                 desired_obstacle_distance, desired_speed):
        """
        Initializes the driver with all necessary components.
        :param steering_component: to compute the steering
        :param speed_component: to compute the speed
        :param color_sensor_component: to read the color or intensity
        :param distance_sensor_component: to read the frontal obstacle distance
        :param desired_obstacle_distance: the desired distance to respect with frontal obstacle in centimeters
        :param desired_speed: the desired speed to reach
        """
        self._steering_component = steering_component
        self._speed_component = speed_component
        self._color_sensor_component = color_sensor_component
        self._distance_sensor_component = distance_sensor_component
        self._desired_obstacle_distance = desired_obstacle_distance
        self._desired_speed = desired_speed
        self._steering = 0
        self._speed = desired_speed


    def update(self, delta_time):
        """
        Updates the driver decisions according to the current delta time.
        :param delta_time: the current delta time in seconds
        """
        direction_error = self._color_sensor_component.read_intensity() - 30
        distance_error = self._distance_sensor_component.read_distance() - self._desired_obstacle_distance
        if self._steering_component is not None:
            self._steering = self._steering_component.compute(direction_error, delta_time)
            #print("new steerin : ",self._steering)
            #self._steering = self._steering*50/30
        if self._speed_component is not None:
            self._speed = self._speed_component.compute(distance_error, delta_time)
            #self._speed = self._speed


    def get_steering(self):
        """
        Returns the current steering.
        :return: the steering
        """
        return self._steering


    def get_speed(self):
        """
        Returns the current speed
        :return: the speed in % in [0;100]
        """
        return self._speed