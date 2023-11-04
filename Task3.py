#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftmotor = Motor(Port.D)
rightmotor = Motor(Port.A)
medium_motor = Motor(Port.B)
robot = DriveBase(leftmotor,rightmotor,wheel_diameter= 55.5, axle_track = 300)
gyro = GyroSensor(Port.S4)


# Write your program here.

def breathe():
    cheer = False
    quo = False
    gyro.reset_angle(0)
    ev3.speaker.say("tripping balls")
    robot.drive(0,30)
    print(gyro.angle())
    while cheer == False:
        robot.drive(100,0)
        if robot.distance() > 400:
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            cheer = True
    while quo == False:
        robot.drive(0,30)
        if gyro.angle() > 78:                
            robot.stop()
            leftmotor.brake()
            rightmotor.brake()
            print(gyro.angle())
            quo = True
    ev3.speaker.say("beep boop beep")
breathe()