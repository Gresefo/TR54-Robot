from umqtt.robust import MQTTClient

import threading

import time

class mqttClient(threading.Thread):

    def __init__(self,id,ip,topic_sub,robot):
        threading.Thread.__init__(self)
        self._client = MQTTClient(id,ip)
        self._client.set_callback(self.getmessages)
        self._client.connect()
        self._client.subscribe(topic_sub, qos = 1)
        self._topic_sub = topic_sub
        self._id = id
        self._robot = robot
        self._delta_time = 1
        self._topics = []
    
    def sendMessage(self, topic, msg, qos=0):
        """
        Sets the message to send
        :param msg : String the message to send
        """
        if(not(topic in self._topics)):
            self._client.subscribe(topic,qos)
            self._topics.append(topic)
        self._client.publish(topic,msg)


    def getmessages(self,topic,msg):
        """
        Gets the message from a topic
        :param topic: the topic to listen
        :param msg: the message to get
        """
        if(topic == bytes(self._topic_sub,'utf-8')):
            print("Here")
            txt = msg.decode('utf-8')
            self._robot.update_List(txt)
            print(txt)

    def run(self):
        """
        The run function for the thread
        """
        while True:
            self._client.check_msg()
            time.sleep(self._delta_time)
