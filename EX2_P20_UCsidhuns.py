#Exam 2 question 20
# File: EX2_P20_UCsidhuns.py
# Date:    8 12 2021
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
# Calculating resistance and conductance of materials.

mat=float(input("Input valid material(1 for Ag, 2 for Ni, 3 for Hg:"))


if mat != 1 and mat != 2 and mat != 3:
    print(" Invalid material has been inputted, resart program ")
    exit()


Length= float(input("Enter length here:"))
Area = float(input("Enter cross-sectional area here:"))

if Area < 0 or Length < 0:
    print("The length and Area must be positive")
    exit()
if mat == 1:
    Re = (1.59e-8*Length)/Area
    G = (6.30e7*Area)/Length
if mat == 2:
    Re = (6.99e-8*Length)/Area
    G = (1.43e7*Area)/Length
if mat == 3:
    Re = (9.80e-7*Length)/Area
    G = (1.02e6*Area)/Length
print( " Resistance(in ohms) = ",Re)
print(" Conductance(in Siemens,S) = ",G)
if Re > 2.4e6:
    print("material is a good insulator")
if G > 1e6:
    print("material is a good conductor")
