from decimal import Decimal, getcontext
getcontext().prec = 2
print('y, x')
y=int(input()) #years
x=float(input()) #every year
a=x/12 #every month
S=Decimal(input())
summ=0
for i in range(y): #0 -> y-1
	summ+=a**i
x = S*Decimal((1+a**y+3*(summ-1))/(a**y+3*summ))a
print(x)
