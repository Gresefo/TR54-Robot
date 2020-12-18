from umqtt.robust import MQTTClient

import threading

import time

class fifoPublisher(threading.Thread):

    def __init__(self,ip,id,s,delta_time):
        """
        Constructor
        :param ip : the IP adresse to connect
        :param id : the robot ID (1, 2 or 3)
        :param s : a string that indicates with information to send in order to get the correct topic
        :param delta_time : the time between two sending of the information
        """
        threading.Thread.__init__(self)
        self._client = MQTTClient(id,ip)
        self._client.connect()
        self._topic = "TR54/g3/listFIFO"
        self._msg = ""
        self._delta_time = delta_time

        self._pub_allowed = False

    def setMessage(self, msg):
        """
        Sets the message to send
        :param msg : String the message to send
        """
        self._msg = msg
        self._pub_allowed = True


    def run(self):
        """
        The run function for the thread
        """
        while True:
            if(self._pub_allowed):
                print("Publishing")
                self._client.publish(self._topic,self._msg)
                self._pub_allowed = False
            else:
                self._client.publish(self._topic,"")
            time.sleep(self._delta_time)

    # def __init__(self,ip,id,s,delta_time):
    #     threading.Thread.__init__(self)
    #     self._client = MQTTClient(id,ip)
    #     self._client.connect()
    #     self._msg = "ah"
    #     self._delta_time = delta_time
    #     self._topic = "TR54/g3/" + s
    #     self._pub_allowed = False

    # def setMessage(self, msg):
    #     self._msg = msg
    #     self._pub_allowed = True

    # def run(self):
    #     while True:
    #         if(self._pub_allowed):
    #             print("Publishing",self._topic," | msg : ",self._msg)
    #             self._client.publish(self._topic,self._msg)
    #             self._pub_allowed = False
    #         time.sleep(self._delta_time)

    



