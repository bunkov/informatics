out = open('float_data.txt', 'r')

summ = 0
sumsqr = 0
float_arr = list(map(float, out.readlines()))
summ = sum(float_arr)/10**6
for i in range(10**6):
    sumsqr += float_arr[i]**2
sigma = (sumsqr/10**6 - summ**2)**0.5

print(summ)
print(sigma)
maxim = max(float_arr)
minim = min(float_arr)
print(maxim, ' ', float_arr.index(maxim))
print(minim, ' ', float_arr.index(minim))
