# HW 10.1 task 2
# File: HW_10p1_Task2_UCsidhuns.py 
# Date:    4/11/2021
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
# This python code will be used to calculate the incident Angle, the reflected angle,
# the transmitted angle, the reflected amplitude, and the transmitted amplitude.
# This is by inputting the intrinsic impedances, the phase constants, and the amplitude.

import math
N1=float(input('Please enter the intrinsic impedance of material 1:'))
B1=float(input('Please enter the phase constant of material 1:'))
N2=float(input('Please enter the intrinsic impedance of material 2:'))
B2=float(input('Please enter the phase constant of material 1:'))
Ei= float(input('Please enter the amplitude of the incident wave (V/m):'))
sin_BA=math.sqrt(((B2**2)*((N2**2)-(N1**2)))/((N2**2)*(B1**2)-(N1**2)*(B2**2)))
BA=math.asin(sin_BA)
Inc= (BA*180)/math.pi
Ref= Inc*1
Cost=(N1*math.cos(BA))/N2
TransR= math.acos(Cost)
Trans=((TransR)*180)/math.pi
AmpT = ((2*N2*math.cos(BA))/(N2*math.cos(TransR)+(N1*math.cos(BA))))*Ei
AmpR=((N2*math.cos(BA)-N1*math.cos(TransR))/(N2*math.cos(BA)+(N1*math.cos(TransR))))*Ei
print('Incident Angle:',Inc)
print('Reflected Angle:', Ref)
print('Reflected Amplitude(V/m):', AmpR)
print('Transmitted Amplitude(V/m):', AmpT)
print('Transmitted Angle',TransR)

