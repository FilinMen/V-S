
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as pl
import plotly.express as px

list_simpl_num =[1,2,3,5,7,11,13,17,19,23,29]
list = []
sov_num = [6,28]
number = int(input("Please Enter any Number: "))  #
for i in range(1, number + 1):                    #
    list.append(int(i))                           #натуральный ряд
print(list)


x = list
y = []
a = 1

for m in list:
    for l in list:
        b = m%l
        if b == 0:
            b = m/l
            a += b
    y.append(a) 
    
list_colorx = []

for q in x:   
    q = int(q)
    if q in list_simpl_num:
        i = 'b'
        list_colorx.append(q)
        list_colorx.append(i)
    elif q in sov_num:
        i = 'r'
        list_colorx.append(q)
        list_colorx.append(i)
    else:
        i = 'g'
        list_colorx.append(q)
        list_colorx.append(i)
print(list_colorx)

list_colory = []
for q in y:   
    q = int(q)
    if q in list_simpl_num:
        i = 'b'
        list_colory.append(q)
        list_colory.append(i)
    elif q in sov_num:
        i = 'r'
        list_colory.append(q)
        list_colory.append(i)
    else:
        i = 'g'
        list_colory.append(q)
        list_colory.append(i)
print(list_colory)

plt.scatter(x = list_colorx, y = list_colory)
plt.legend(loc = 'upper right')
plt.xlabel('Sum of divisors of number') #Подпись для оси х
plt.ylabel('Sum of the divisors of a number') #Подпись для оси y
plt.title('Types of numbers') #Название
plt.show()
