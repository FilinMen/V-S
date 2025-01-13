# отображение точек из натурального ряда


import matplotlib.pyplot as plt

list = []
sov_num = [6,28,496,8128]
x = list
y = []
x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []


def is_simpl(x):#проверка числа на простое 
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def listx(): #перебор элементов из списка y
    for i in y:
        return i

def sumdel(m): #подсчет суммы делителей
    a = 0
    for l in range(1,max(list)):
        b = m%l
        if b == 0:
            a += l
        elif is_simpl(m) == True:
            a = 1 
    y.append(int(a)) 

def Naturalrow(x): #натуральный ряд
    for i in range(1, x + 1):                    
        list.append(int(i))                           

def color(): # распределение цветов 
    for q in x: 
        i = listx()  
        q = int(q)
        i = int(i)
        if is_simpl(q) == True:#green
            y1.append(i)
            x1.append(q)
        elif q in sov_num:#red
            y2.append(i)
            x2.append(q)
        else:#blue
            y3.append(i)
            x3.append(q)
        y.remove(i)

def plo(): # отрисовка графика
    plt.scatter(x1, y1, color = 'g', label = 'simpl_num')
    plt.scatter(x2, y2, color = 'r', label = 'sov_num')
    plt.scatter(x3, y3, color = 'b', label = 'another')
    plt.legend(title = 'types of number')
    plt.xlabel('Sum of divisors of number') #Подпись для оси х
    plt.ylabel('Sum of the divisors of a number') #Подпись для оси y
    plt.title('Types of numbers') #Название
    plt.grid()
    plt.show()

def main(): 
    number = int(input("Please Enter any Number: "))
    Naturalrow(number)
    for m in list:
        sumdel(m)
    color()
    plo()

if __name__ == "__main__":
    main()
