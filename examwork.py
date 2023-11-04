import math

IntV=float(input("enter initial velocity here:"))
AngleIncr= float(input("enter the angle increment here:"))

while IntV < 0:
    IntV = float(input(" velocity entered is outof range, please enter a positive velocity:"))

while AngleIncr < 0 or AngleIncr > 90:
    AngleIncr = float(input(" Angle increment is out of range, enter correct angle increment:"))

Angleloop=0

while Angleloop <= 90:
    Angleloop = Angleloop + AngleIncr
    AngleRad = AngleIncr * (math.pi)/180
    
    MaxH= (IntV**2)*(math.sin(AngleRad)**2)/ (2*9.81)

    ImpactT = ((2*IntV * (math.sin(AngleRad))))/9.81

    print(' Max Height = {0:.2f} m, Impact time = {1:.2f} s '.format(MaxH,ImpactT))
    if AngleIncr > 85:
        break
    
