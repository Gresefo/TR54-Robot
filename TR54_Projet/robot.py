from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

class robot:
    """ Defines a robot with a driver component. """

    def __init__(self, controller_component, driver_component, id, init_map_location=0):
        """
        Initializes the robot with the given controller and components.
        :param controller_component: the controller component that controls wheel motors
        :param driver_component: the driver component to decide how to drive
        :param init_map_location: int to indicate where the robot starts on the map
        """
        self._controller = controller_component
        self._driver = driver_component
        self._id = id

        #variables pour localiser le robot
        #self._map = [['A',0],['B',1],['C',0],['D',2],['E',0],['F',2],['G',0],['H',1]]
        self._map = [['A',90],['B',45],['C',45],['D',90],['E',45],['F',90],['G',45],['H',90]]
        self.map_location = init_map_location
        self.action = self._map[self.map_location][1]
        self._controller.action = self.action
        self._recorded_angle = 0

        #variables pour la gestion des messages MQTT
        self.allowed = True

        #variable pour l'ordonnancement
        self.waiting_list = []
        self.intersection = 0

        #gestion couleur
        self.ev3 = EV3Brick()
        self.ev3.light.on(Color.YELLOW)

    def isInWaitingList(self, msg_id):
        """
        Indicates if the ID is already in the waiting list, to know if we need to add it, or to remove it
        :param msg_id: int the ID to check
        """
        for robot_id in self.waiting_list:
            if(robot_id == msg_id):
                return True
        return False

    def update_List(self, id):
        if(id!=""):
            msg_id = int(id)

            #If the ID received is already in the waiting list, we remove it
            if(self.isInWaitingList(msg_id)):
                #Check if the ID to remove is the first one
                if(self.waiting_list[0] == msg_id):
                    print("popping")
                    self.waiting_list.pop(0)
                    
                else:
                    print("Error, asked to remove an ID in FIFO list that is not the first")
            #If the ID received is not in the waiting list, we add it at the end
            else:
                self.waiting_list.append(msg_id)
                print("ajout")
            print(self.waiting_list)
            if(len(self.waiting_list) > 0):
                if(self.waiting_list[0] == int(self._id)):
                    print("allowing")
                    self.ev3.light.on(Color.GREEN)
                    self.allowed = True

    def update_Color(self,color):
        self.ev3.light.on(color)


    def drive(self, delta_time):
        """
        Drives the robot according to the given delta time.
        :param delta_time: the delta time in seconds.
        """
        if(self.allowed):
            self._driver.update(delta_time)
            self._controller.drive(self._driver.get_steering(),self._driver.get_speed())
            
            # "new_action = self._controller.action"
            # if(self.action != new_action):
            #     predicted_action = self._map[(self.map_location+1)%len(self._map)][1]
            #     if(new_action == predicted_action):
            #         self.map_location = (self.map_location+1)%len(self._map)
            #         #print(self._map[self.map_location][0])
            #         #publish self._map[self.map_location][0]
            #     else:
            #         print("wrong action predicted, not forwarded to map location")
            # print(self._controller.current_angle - self._recorded_angle)
            if(abs(self._controller.current_angle - self._recorded_angle) > self._map[self.map_location][1]):
                self._recorded_angle = self._controller.current_angle
                self.map_location = (self.map_location+1)%len(self._map)
                print(self._map[self.map_location][0])
                
                


            self.action = self._controller.action
        else:
            self.stop()


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