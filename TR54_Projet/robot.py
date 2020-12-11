class robot:
    """ Defines a robot with a driver component. """

    def __init__(self, controller_component, driver_component):
        """
        Initializes the robot with the given controller and components.
        :param controller_component: the controller component that controls wheel motors
        :param driver_component: the driver component to decide how to drive
        """
        self._controller = controller_component
        self._driver = driver_component

    def drive(self, delta_time):
        """
        Drives the robot according to the given delta time.
        :param delta_time: the delta time in seconds.
        """
        self._driver.update(delta_time)
        self._controller.drive(self._driver.get_steering(),self._driver.get_speed())

    def stop(self):
        """
        Stops the robot.
        :return:
        """
        self._controller.stop()

    def get_controller(self):
        """
        Returns the controller of the robot.
        :return: the controller
        """
        return self._controller

    def get_driver(self):
        """
        Returns the driver of the robot.
        :return: the driver
        """
        return self._driver
