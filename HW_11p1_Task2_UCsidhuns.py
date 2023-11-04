# HW 11.1 task 2
# File: HW_11p1_Task2_UCsidhuns.py 
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
# break is needed. If a break is needed, how long should that break be and how many breaks?
T=float(input('Enter outside temperature:'))
Wc=int(input('Enter weather conditions, 3 if sunny, 2 if cloudy, 0 if Raining:'))
H = float(input('Enter Relative Humidity:'))
if T>125 or T < -10:
    print('error, input outside range of model',T)
    exit("End program due to value being out of range")
if Wc != 3 and Wc != 2 and Wc != 0:
    print('error, input outside range of model',Wc)
    exit("End program due to value being out of range")
if H< 0 or H>1:
    print('error, input outside range of model',H)
    exit("End program due to value being out of range")
if Wc == 0:
    print('Work Inside')
    exit("End program due to value being out of range")
if T>= 90 and H> 0.8:
    print(' give two 15 minute breaks')
if T>= 90 and H> 0.9:
    print(' give one 15 minute breaks')
if T >=90 and H<0.8:
    print('give one 10 minute break')
if T>80 and T < 90 and H>0.9 and Wc == 3:
    print(' give two 10 minute breaks')
if T>80 and T < 90 and( H>0.9 or Wc == 3):
    print(' give one 10 minute breaks')
if T< 80:
    print(' no extra breaks')
    

       
