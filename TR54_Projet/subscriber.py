from pybricks import ev3brick as brick

import threading

from umqtt.robust import MQTTClient
import time

class subscriber(threading.Thread):

    def getmessages(self,topic,msg):
        print(type(topic))
        print(type(self._topic))
        if bytes(self._topic,'utf-8') == topic:
            brick.display.text(msg.decode('utf-8'))
            txt = msg.decode('utf-8')
            print(msg.decode('utf-8'))
            splt = txt.split('|')
            if(len(splt) >1 ):
                print(splt[1])
            if(splt[0]=="stop"):
                self.robot.allowed = False
            elif(splt[0]=="go"):
                self.robot.allowed = True
                

    def __init__(self,ip,id,topic,robot):
        threading.Thread.__init__(self)
        self._client = MQTTClient(id,ip)
        self._client.connect()
        self._client.set_callback(self.getmessages)
        self._client.subscribe(topic)
        self._topic = topic

        self.robot = robot

    def run(self):
        self._client.publish(self._topic,'Listening')
        brick.display.text('Listening...')
        while True:
            self._client.check_msg()
            time.sleep(0.1)
