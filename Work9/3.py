from decimal import *
S=int(input()) # Сумма
x=int(input()) # Годовой %
y=int(input()) # Кол-во лет

n=y*12 # Кол-во месяцев
quota = Decimal(x/100/12).quantize(Decimal('.000001'))
increasing_factor = quota + 1
payment=S*increasing_factor**n*(increasing_factor-1)/(increasing_factor**n-1)
payment=Decimal(payment).quantize(Decimal('.01'))
print('Аннуитетный платеж',payment)
print('Переплата',Decimal(payment*n-S).quantize(Decimal('.01')))

print('Месяц ||','Остаток ||','Платеж ||','На проценты ||','На основную сумму')
ostatok=Decimal(S).quantize(Decimal('.01'))
for i in range(1,n+1):
	upbuilding=Decimal(ostatok*quota).quantize(Decimal('.01'))
	if ostatok + upbuilding <= payment:
		payment = ostatok + upbuilding
	na_dolg = payment - upbuilding
	ostatok += upbuilding - payment
	print(i, '||',ostatok, '||',payment, '||',upbuilding,'||',na_dolg)
