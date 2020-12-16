from umqtt.robust import MQTTClient

import threading

import time

class publisher(threading.Thread):

    def __init__(self,ip,id,s,delta_time):
        threading.Thread.__init__(self)
        self._client = MQTTClient(id,ip)
        self._client.connect()
        if(id !== ""):
            self._topic = "TR54/g3/r" + id +"/" + s
        else:
            self._topic = "TR54/g3/" + s
        self._msg = ""
        self._delta_time = delta_time

    def setMessage(self, msg):
        self._msg = msg


    def run(self):
        while True:
            self._client.publish(self._topic,self._msg)
            time.sleep(self._delta_time)