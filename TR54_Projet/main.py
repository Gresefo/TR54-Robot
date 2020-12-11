#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

AXE_DIAMETER = 186 #mm
WHEEL_DIAMETER = 35 #mm

import time
from pybricks.tools import wait

from twoWheelsController import *
from basicDriver import *
from basicPIDComponent import *
from colorSensor import *
from distanceSensor import *
from robot import *

from subscriber import *

MIN_DELTA_TIME = 0.1

OUTPUT_A = Port.B
OUTPUT_B = Port.C
INPUT_1 = Port.S3
INPUT_2 = Port.S2

robot = robot(
    controller_component=twoWheelsController(
        left_motor_output=OUTPUT_A, right_motor_output=OUTPUT_B,
        min_steering=-360, max_steering=360,
        min_speed=0, max_speed=100,
        wheelDiameter=WHEEL_DIAMETER, axeDiameter=AXE_DIAMETER
    ),
    driver_component=basicDriver(
        steering_component=basicPIDComponent(kp=0.4, ki=0.4, kd=0.01),
        speed_component=basicPIDComponent(kp=0.4, ki=0.4, kd=0.01),
        color_sensor_component=colorSensor(sensor_input=INPUT_1),
        distance_sensor_component=distanceSensor(sensor_input=INPUT_2),
        desired_obstacle_distance=15,
        desired_speed=100
    )
)


start_time = time.time()
last_time = start_time
last_delta_time = MIN_DELTA_TIME
count = 0

while True:
    # Drives the robot
    robot.drive(last_delta_time)

    # Computes the time used to execute the drive method
    drive_time = time.time() - last_time

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