# HW 12.1 task 1
# File: HW_12p1_Task1_UCsidhuns.py 
# Date:    11/18/2021
# By:      Nihaal Sidhu
# Section: 016
# Team:    228
# 
# ELECTRONIC SIGNATURE
# Nihaal Sidhu
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#Projectile motion, calculating maximum height and the time the projectile impacts
#the ground.

import math
Vo=float(input('enter initial velocity here:'))
Incr=float(input('enter angle increment here:'))
while Vo<0:
    Vo=float(input('Initial velocity entered is invalid. /n Enter new velocity here:'))
while Incr< 0 or Incr>90:
    Incr=float(input('Initial Angle increment entered is invalid. /n Enter new Angle Increment here:'))
IncrAng=0
while IncrAng <= 90:
    IncrAng=IncrAng + Incr
    Angleincrad = IncrAng * (math.pi)/180
    
    MaxHeight =(Vo**2)*(math.sin(Angleincrad)**2)/(2*9.81)
    Imp_time = (2*(Vo))*(math.sin(Angleincrad))/9.81
    print( ' Max Height = {0:.2f} m, Impact Time = {1:.2f} s '.format(MaxHeight,Imp_time))
    if IncrAng > 85:
        break
    
