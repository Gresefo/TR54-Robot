from pybricks import ev3brick as brick
from umqtt.robust import MQTTClient
import threading
import time

class subscriber(threading.Thread):
    """Thread to listen to the MQQT messages"""

    def getmessages(self,topic,msg):
        """
        Gets the message froma topic
        :param topic: the topic to listen
        :param msg: the message to get
        """
        #print(type(topic))
        #print(type(self._topic))
        #topic = getTopicFromId(self, s)
        if bytes(self._topic,'utf-8') == topic:
            brick.display.text(msg.decode('utf-8'))
            txt = msg.decode('utf-8')
            #print(msg.decode('utf-8'))
            #splt = txt.split('|')
            #if(len(splt) >1 ):
            #    print(splt[1])
            """if(splt[0]=="stop"):
                self.robot.allowed = False
            elif(splt[0]=="go"):
                self.robot.allowed = True"""
            cur_id = int(txt)
            isWaiting = False
            for robot_id in robot.waiting_list:
                if(robot_id == cur_id):
                    isWaiting = True
            if(not(isWaiting)):
                robot.waiting_list.append(cur_id)
            else:
                robot.waiting_list.pop(0)
            
            if(robot.waiting_list[0]==self.id):
                robot.allowed=True

            
                

    def __init__(self,ip,id,topic,robot):
        """
        Constructor
        :param ip: the IP adresse to connect
        :param id: the robot ID (1, 2 or 3)
        :param topic: the topic to listen
        :param robot: the current robot
        """
        threading.Thread.__init__(self)
        self._client = MQTTClient(id,ip)
        self._client.connect()
        self._client.set_callback(self.getmessages)
        self._client.subscribe(topic)
        self._topic = topic
        self.id = id
        self.robot = robot


    def run(self):
        """
        The run function for the thread
        """
        self._client.publish(self._topic,'Listening')
        brick.display.text('Listening...')
        while True:
            self._client.check_msg()
            time.sleep(1)
    
