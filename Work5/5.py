from random import *

int_d = open('int_data.txt', 'w')
for i in range(10**6):
    int_d.write(str(randint(0, 100)) + '\n')

float_d = open('float_data.txt', 'w')
for i in range(10**6):
    float_d.write(str(randint(0, 10000)/100) + '\n')
