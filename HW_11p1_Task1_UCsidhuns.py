# HW 11.1 task 1
# File: HW_11p1_Task1_UCsidhuns.py 
# Date:    11/11/2021
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
#
# This program is coded for the user to input values in a workplace to determine wether or not an extra
# break is needed or if the site manager needs to hold a quick safety meeting. 
import sys
T=float(input('Enter outside Temperature:'))
Wc=int(input('Enter the Weather conditions,3 for sunny,2 if partly cloudly,0 for cloudy:'))
H=float(input('Enter the Relative Humidity:'))
L=int(input('Number of ladders on construction site:'))
Hstruc=float(input('Height of structure:'))
Sdry=int(input('Surface dryness, 3 if all surfaces wet, 2 if puddles, 0 if surface dry:'))

if T>125 or T < -10:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
if Wc != 3 and Wc != 2 and Wc != 0:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
if H< 0 or H>1:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
if L<0:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
if Hstruc> 2800 or Hstruc<20:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
if Sdry !=3 and Sdry != 2 and Sdry !=0:
    print('error, input outside range of model')
    exit("End program due to value being out of range")
HRI = (0.75*T)+ (5*Wc)+ (H**2)
if HRI>75:
    Hcat=1
else:
    Hcat = 0
FRI = (0.2 *L)+(0.03*Hstruc)+(30*Hcat)+(10*Sdry)
print('HRI value: {0:0.1f}/n'.format (HRI))
print('FRI value: {0:0.1f}/n'.format (FRI))
if HRI > 75:
    print('Allow 1 extra break')
if FRI>100:
    print('site manager needs to hold a quick safety session to remind workers of proper procedures to reduce injuries')
if HRI < 75 and FRI < 100:
    print(' Safety is Job #1')



