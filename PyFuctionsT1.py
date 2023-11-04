def Ifitworks(K1,K2,Ftotal,Mean):
    if Mean == 'Series':
        keq = (1/K1)+(1/K2)
        F1 = Ftotal
        F2 = Ftotal
        Xtotal = Ftotal/keq
        X1 = F1/K1
        X2 = F2/K2
      
    else:
        keq = K1 + K2
        Xtotal = Ftotal / keq
        Xtotal = X1 = X2
        F1 = K1 * X1
        F2 = K2 * X2
    return keq , X1, X2, F1, F2, Xtotal
    


K1= int(input("input K1 value:"))
K2 = int(input("input K1 value:"))
Ftotal = int(input("input Force total value here"))
Mean = input(' Input type of spring, Series or Parallel')

Variable =Ifitworks(K1, K2, Ftotal, Mean)

print(Variable)
