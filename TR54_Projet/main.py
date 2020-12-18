#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port
import time
from pybricks.tools import wait

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

from twoWheelsController import *
from basicDriver import *
from basicPIDComponent import *
from basicOnePointComponent import *
from colorSensor import *
from distanceSensor import *
from robot import *
from subscriber import *
from publisher import *

from fifoPublisher import *

from mqttClient import mqttClient

"""
Global variables
"""
AXE_DIAMETER = 186 #mm
WHEEL_DIAMETER = 35 #mm
MIN_DELTA_TIME = 0.1 #s

OUTPUT_A = Port.B
OUTPUT_B = Port.C
INPUT_1 = Port.S3
INPUT_2 = Port.S2

IP = "192.168.43.93" #IP adresse to connect to get the MQQT broker
ID = "1" #The ID of this robot


print("start")

#publisher_speed = publisher(ip=IP,id=ID,s="vitesse",delta_time=1)
#publisher_action = publisher(ip=IP,id=ID,s="action",delta_time=1)
#publisher_position = publisher(ip=IP,id=ID,s="position",delta_time=0.25)
#publisher_fifo = publisher(ip=IP,id=ID,s="fifo",delta_time=0.25)
#publisher_fifo = fifoPublisher(ip=IP,id=ID)


robot = robot(
    controller_component=twoWheelsController(
        left_motor_output=OUTPUT_A, right_motor_output=OUTPUT_B,
        min_steering=-360, max_steering=360,
        min_speed=0, max_speed=200,
        wheelDiameter=WHEEL_DIAMETER, axeDiameter=AXE_DIAMETER
    ),
    driver_component=basicDriver(
        steering_component=basicPIDComponent(kp=0.31, ki=0.25, kd=0.00225),
        speed_component=basicOnePointComponent(acceleration=2.1,max_speed=150),
        color_sensor_component=colorSensor(sensor_input=INPUT_1),
        distance_sensor_component=distanceSensor(sensor_input=INPUT_2),
        desired_obstacle_distance=30,
        desired_speed=100
    ),
    id=ID
)

mqttClient_1 = mqttClient(id=ID,ip=IP,topic_sub="TR54/g3/listFIFO",robot=robot)
#subscriber = subscriber(ip=IP,id=ID,topic=b"TR54/g3/listFIFO",robot=robot)

start_time = time.time()
last_time = start_time
last_delta_time = MIN_DELTA_TIME
count = 0


#publisher_speed.start()
#publisher_position.start()
#publisher_action.start()
#publisher_fifo.start()
mqttClient_1.start()
#subscriber.start()

while True:
    # Drives the robot
    robot.drive(last_delta_time)


    # Computes the time used to execute the drive method
    drive_time = time.time() - last_time
    #publisher_speed.setMessage(str(int(robot.get_driver().get_speed())))
    #publisher_position.setMessage(robot._map[robot.map_location][0])
    #publisher_action.setMessage(robot._controller.current_action[robot._controller.action])
    #mqttClient_1.sendMessage("TR54/g3/r"+ID+"/vitesse",str(int(robot.get_driver().get_speed())))
    #mqttClient_1.sendMessage("TR54/g3/r"+ID+"/position",robot._map[robot.map_location][0])
    #mqttClient_1.sendMessage("TR54/g3/r"+ID+"/action",robot._controller.current_action[robot._controller.action])
    if(robot._map[robot.map_location][0]=='G' or robot._map[robot.map_location][0]=='C'):
        if(robot.intersection==0):
            print("G ou C")
            robot.intersection=1
            robot.allowed = False
            robot.ev3.light.on(Color.RED)
            #publisher_fifo.setMessage(ID)
            #publisher_fifo.fifoPublish(ID)
            mqttClient_1.sendMessage("TR54/g3/listFIFO",ID,1)
    elif(robot._map[robot.map_location][0]=='H' or robot._map[robot.map_location][0]=='D'):
        if(robot.intersection == 1):
            print("Arrive a D")
            robot.intersection=2
            robot.ev3.light.on(Color.YELLOW)
            mqttClient_1.sendMessage("TR54/g3/listFIFO",ID,1)
            #publisher_fifo.fifoPublish(ID)
    else:
        robot.intersection = 0
        robot.ev3.light.on(Color.YELLOW)
        #print("remise a 0")
    # Computes the necessary time to sleep to fix delta time
    sleep_time = max(0.0, MIN_DELTA_TIME - drive_time)
    # Sleeps to force respecting the min delta time
    #sleep(sleep_time)
    time.sleep(sleep_time)

    # Updates info
    current_time = time.time()
    last_delta_time = current_time - last_time
    last_time = current_time
    count += 1
    elapsed_time = current_time - start_time
    average_delta_time = elapsed_time / count