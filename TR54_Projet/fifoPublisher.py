from umqtt.simple import MQTTClient

import time

class fifoPublisher:

    def __init__(self,ip,id):
        """
        Constructor
        :param ip : the IP adresse to connect
        :param id : the robot ID (1, 2 or 3)
        """
        self._client = MQTTClient(id,ip)
        self._client.connect()
        self._topic = "TR54/g3/listFIFO"
        

    def fifoPublish(self, msg):
        print("publish:", msg)
        try:
            self._client.publish(self._topic, msg, retain = false, qos = 1)
        except:
            print("probleme fifo pubish try catch")
    



