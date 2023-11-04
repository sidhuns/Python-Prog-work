ph= float(input('enter ph level here:'))
if ph > 14:
    print('invalid')
elif ph > 7:
    print('basic')
elif ph == 7:
    print( ' neutral')
elif ph > 0:
    print(' acidic ')
else:
    print('invalid')
