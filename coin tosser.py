import random
coin=int(input('enter the number of times coin shall be flipped:'))
total=0
d=0
for total in range(coin):
    flip = random.randint(1,2)
    if flip == 1:
        d=d+1
tails=coin-d
PT=tails/coin*100
PH=d/coin*100
print('amount landed heads'+str(d))
print('amount landed tails'+str(tails))
print('percent tails{0:0.2f}'.format(PT))
print('percent heads{0:0.2f}'.format(PH))


    


    
