#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftmotor = Motor(Port.D)
rightmotor = Motor(Port.A)
medium_motor = Motor(Port.B)
robot = DriveBase(leftmotor,rightmotor,wheel_diameter= 55.5, axle_track = 300)
gyro = GyroSensor(Port.S4)

def tasker():
    cheerd = False
    cheerds = False
    quot = False
    chid = False
    chuck = False
    chids = False
    while quot == False:
        robot.drive(0,30)
        if gyro.angle() > 172:                
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            print(gyro.angle())
            quot = True
    while cheerd == False:
        robot.drive(100,0)
        if robot.distance() > 202.5:
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            cheerd = True
    gyro.reset_angle(0)
    while chid == False:
        robot.drive(0,-30)
        if gyro.angle() < -79.2:                
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            print(gyro.angle())
            chid = True
    while cheerds == False:
        robot.drive(100,-.4)
        if robot.distance() > 2696:
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            cheerds = True
    gyro.reset_angle(0)
    while chids == False:
        robot.drive(0,-30)
        if gyro.angle() < -79.5:                
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            print(gyro.angle())
            chids = True
    while chuck == False:
        robot.drive(100,0)
        if robot.distance() > 2899.5:
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            chuck = True
tasker()
