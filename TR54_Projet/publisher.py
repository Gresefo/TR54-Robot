from umqtt.robust import MQTTClient

import threading

import time

class publisher(threading.Thread):
    """A thread to pusblish information using a MQQT broker"""

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
        self._topic = "TR54/g3/r" + id +"/" + s
        self._msg = ""
        self._delta_time = delta_time
        if(s =="fifo"):
            self._topic = "TR54/g3/listFIFO"

    def setMessage(self, msg):
        """
        Sets the message to send
        :param msg : String the message to send
        """
        self._msg = msg


    def run(self):
        """
        The run function for the thread
        """
        while True:
            self._client.publish(self._topic,self._msg)
            time.sleep(self._delta_time)