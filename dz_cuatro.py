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

# Задача 3. Задайте последовательность чисел. 
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
        coef = random.ransdint(0, 100)
        lst.append(coef)
    if lst[0] != 0:
        if lst[1] == 0 and lst[2] != 0:
            result = ('{}x^{} + {}'.format(lst[0], k, lst[2]))
        elif lst[2] == 0 and lst[1] != 0:
            result = ('{}x^{} + {}'.format(lst[0], k, lst[1]))
        elif lst[1]== 0 and lst[2] == 0:
            result = ('{}x^{}'.format(lst[0], k, lst[2]))
        else:
            result = '{}x^{} + {}x + {}'.format(lst[0], k,  lst[1], lst[2])
        return result
    else:
        return "Try again"
m = my_func(2)
print (m)

f = open('my_file.txt', 'w')
f.write(m)
f.close()

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
with open('my_file2.txt', 'w') as f_new:
    f_new.write('2x^2 + 4x + 5')
f_new = open('my_file2.txt', 'r')
read = f_new.read()
f_new.close()

f_old = open ('my_file.txt', 'r')
read1 = f_old.read()
f_old.close()

def get_ones(line):
    tmp = []
    last = 0
    positive = True
    for i, item in enumerate(line):
        if item in {'+', '-'}:
            if positive:
                tmp.append(line[last:i])
            else:
                tmp.append('-' + line[last:i])
            last = i + 1
            positive = item == '+'
 
    if positive:
        tmp.append(line[last:])
    else:
        tmp.append('-' + line[last:])
    return tmp
 
 
def get_coef(one):
    for i, item in enumerate(one):
        if item == 'x':
            return int(one[:i]), one[i:]
    return int(one), None
 
 
lst1 = get_ones(read.replace(' ', '').replace('*', ''))
lst2 = get_ones(read1.replace(' ', '').replace('*', ''))
 
dct1 = {item[1]: item[0] for item in map(get_coef, lst1)}
dct2 = {item[1]: item[0] for item in map(get_coef, lst2)}

 
print(dct1)
print(dct2)

lst1 = list(dct1.values())
lst2 = list(dct2.values())
print(lst1)
print (lst2)

for i in lst1:
    lst3 = []
    n = 0
    for k in lst2:
        k = 0
        b = lst1[n] + lst2[k]
        lst3.append(b)
        n += 1
        k += 1
print (lst3)

# Записываем сумму многочленов в новый файл
with open('final_file.txt', 'w') as another_f:
    another_f.write('{}x^2 + {} + {}'. format(lst3[0], lst3[1], lst3[2]))



        
