# Activity Python CFU: conditional
# File: CFU_11p1_UCsidhuns.py 
# Date:    2 November 2021
# By:       Nihaal Sidhu
# Section: 16
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
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.


AQI= int(input('enter your AQI value here:'))
if AQI > 500:
    print('invalid entry')
elif AQI > 400:
    print(' severe ')
elif AQI > 300:
    print(' very poor')
elif AQI > 200:
    print('poor')
elif AQI > 100:
    print('moderate')
elif AQI > 50:
    print('satisfactory')
elif AQI > 0:
    print('good')
else:
    print('invalid entry')
    
    
    
