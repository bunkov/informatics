from decimal import *
def f_1(y,z):
    return Decimal(108)-(Decimal(815)-Decimal(1500)/z)/y
getcontext().prec=42 # максимальная точность
X=[]
X.append(Decimal(4))
X.append(Decimal(4.25))
for i in range(2,31):
    X.append(f_1(X[i-1],X[i-2]))
print ('Decimal',X[30])

from fractions import Fraction
def f_2(y,z):
    return 108-Fraction(815-Fraction(1500,z), y)
X=[]
X.append(Fraction('4'))
X.append(Fraction('4.25'))
for i in range(2,31):
    X.append(f_2(X[i-1],X[i-2]))
print('Fraction', float(X[30]))
print('(',X[30],')',sep='')