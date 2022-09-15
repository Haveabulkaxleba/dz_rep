#Задача 1. Вычислить число π c заданной точностью d

ddd = float(input())
def pi_number(ddd):
    n = 0
    summ2 = 0
    summ1 = 4
    while abs(summ1 - summ2) >= ddd:
        summ2 = summ2 + 4*((-1)**(n))/(2*n+1)
        summ1 = summ2 + 4*((-1)**(n+1))/(2*n+2)
        n += 1
    return round (summ2/ddd)*ddd
print (pi_number(ddd))

#Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numberrr = int(input ('Число: '))
def fac (a):
    lst = []
    n = 2
    while n*n <= a:
        if a % n == 0:
            lst.append(n)
            a = a//n
        else:
            n += 1
    if a > 1:
        lst.append(a)
    return lst
print (fac(numberrr))

#Задача 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
number = input('Введите последовательность чисел: ').split()
def non_repeat (n):
    lst = list(n)
    new = []
    for i in lst:
        if lst.count(i) == 1:
            new.append(i)
    return new
print (non_repeat(number))

# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
lst = []
def my_func(k):
    global lst
    for i in range (0, 3):
        coef = random.randint(0, 100)
        lst.append(coef)
    if lst[0] != 0:
        if lst[1] == 0 and lst[2] != 0:
            result = ('{}x^{} + {} = 0'.format(lst[0], k, lst[2]))
        elif lst[2] == 0 and lst[1] != 0:
            result = ('{}x^{} + {} = 0'.format(lst[0], k, lst[1]))
        elif lst[1]== 0 and lst[2] == 0:
            result = ('{}x^{} = 0'.format(lst[0], k, lst[2]))
        else:
            result = '{}x^{} + {}x + {} = 0'.format(lst[0], k,  lst[1], lst[2])
        return result
    else:
        return "Try again"
m = my_func(2)
print (m)

f = open('my_file.txt', 'w')
f.write(m)
f.close()