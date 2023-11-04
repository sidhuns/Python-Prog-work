# HW 10.1 task 1
# File: HW_10p1_Task1_UCsidhuns.py 
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
#
# This program is coded for the user to enter the amplitude of the wave,
# the permittivity and the permeability of medium 1 and 2 to calculate the intrinsic
# impedances of the two media and the amplitudes of the reflected and transmitted waves.
E1=float(input('Please enter the relative permittivity of material 1:'))
E2=float(input('Please enter the relative permittivity of material 2:'))
U1=float(input('Please enter the relative permeability of material 1:'))
U2=float(input('Please enter the relative permeability of material 2:'))
Ei=float(input('Please enter the amplitude of the incident wave (V/m):'))
N1=377.14*((U1/E1)**.5)
N2=377.14*((U2/E2)**.5)
ET=((2*N2)/(N2+N2))*Ei
Er=((N2-N1)/(N2+N1))*Ei
print('Reflected Amplitude(V/m):',Er)
print('Transmitted Amplitude(V/m):',ET)
print('Intrinsic Impedance 1(Ohms):',N1)
print('Intrinsic Impedance 1(Ohms):',N2)
