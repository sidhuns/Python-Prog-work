# Exam 2 question 21
# File: EX2_P21_UCsidhuns.py
# Date:    8 12 2021
# By:      Nihaal Sidhu
# Section: 016
# Team:    228
# 
# ELECTRONIC SIGNATURE
# Nihaal Sidhu.
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program is a header template that will be used for 
# all your python files the rest of the semester.
import math

A=float(input("Input the constant,A:"))
if abs(A)>= 1:
    print(" Y value will not converge")
    exit()

rawy=0
loop = 0
Yo = 30
C = 25
rawint=0
cooly = 0
while abs((cooly-C)/(1-A)) > 0.05:
    rawint= rawint+ 0
    loop = loop + 1
    rawy = rawy + Yo
    cooly=(A*rawy)+C
    print(" y value = {0:0.2f} , amount of times y was updated = {1:2f}".format(cooly,loop))
   
        
