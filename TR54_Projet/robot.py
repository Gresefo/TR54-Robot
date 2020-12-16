class robot:
    """ Defines a robot with a driver component. """

    def __init__(self, controller_component, driver_component, init_map_location=0):
        """
        Initializes the robot with the given controller and components.
        :param controller_component: the controller component that controls wheel motors
        :param driver_component: the driver component to decide how to drive
        :param init_map_location: int to indicate where the robot starts on the map
        """
        self._controller = controller_component
        self._driver = driver_component

        #variables pour localiser le robot
        self._map = [['A',0],['B',1],['C',0],['D',2],['E',0],['F',2],['G',0],['H',1]]
        self.map_location = init_map_location
        self.action = self._map[self.map_location][1]
        self._controller.action = self.action

        #variables pour la gestion des messages MQTT
        self.allowed = True

        #variable pour l'ordonnancement
        self.waiting_list = []

        

    def drive(self, delta_time):
        """
        Drives the robot according to the given delta time.
        :param delta_time: the delta time in seconds.
        """
        if(self.allowed):
            self._driver.update(delta_time)
            self._controller.drive(self._driver.get_steering(),self._driver.get_speed())
            
            new_action = self._controller.action
            if(self.action != new_action):
                predicted_action = self._map[(self.map_location+1)%len(self._map)][1]
                if(new_action == predicted_action):
                    self.map_location = (self.map_location+1)%len(self._map)
                    #print(self._map[self.map_location][0])
                    #publish self._map[self.map_location][0]
                else:
                    print("wrong action predicted, not forwarded to map location")

            self.action = self._controller.action
        else:
            self.robot.stop()


    def stop(self):
        """
        Stops the robot
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