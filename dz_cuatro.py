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

#Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
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

#Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
number = input('Введите последовательность чисел: ').split()
def non_repeat (n):
    lst = list(n)
    new = []
    for i in lst:
        if lst.count(i) == 1:
            new.append(i)
    return new
print (non_repeat(number))

