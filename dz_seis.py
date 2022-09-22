# Предложить улучшения кода для уже решённых задач (4 задачи из любых семинаров, кроме первого):
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

# 1) Задача 1 из второго дз. Программа, которая принимает на вход вещественное число и показывает сумму его цифр.
# Старое решение:
num = list(input("Введите число: "))
answer = 0
if "." in num:
    num.remove(".")
    for i in num:
        if i.isdigit:
            answer += int(i)
elif "," in num:
    num.remove(",")
    for i in num:
        if i.isdigit:
            answer += int(i)
elif "-" in num:
    num.remove("-")
    for i in num:
        if i.isdigit:
            answer += int(i)
else:
    for i in num:
        if i.isdigit:
            answer += int(i)

print (answer)

# Новое решение
def summ(num):
    lst = [int(i) if i.isdigit() else i for i in num] # List comprehension
    for item in lst:
        if item == str(item):
            lst.remove(item)
            result = sum(lst)
    return result
    
print(summ(input('Введите число: ')))

# 2) Задача 3 из второго дз. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Старое решение
n = 6
lst = []
for (i) in range (1, n+1):
    i = (1+1/i)**i
    lst.append(i)
    i += 1
print (lst)
print (round(sum(lst), 3))

# Новое решение
n = 6
lbd = lambda x: (1 + 1 / x)**x # Лямбда
lst = [lbd(x) for x in range(1, n + 1)] # List comprehension
print(lst)
print(round(sum(lst), 3))

# 3) Задание 4 из второго дз. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.

# Старое решение
n = int(input ("N = "))    
a = int(input ("a = "))
b = int(input ("b = "))
lstN = list(range(n+1))
lst_negative_N = []
for i in lstN:
    k = int(i) * -1
    lst_negative_N.append(k)
    newlist = list(reversed(lst_negative_N))
del newlist[len(newlist)-1]
generalL = newlist + lstN
print(generalL)
mult = generalL [a-1] * generalL [b-1]
print (mult)

# Новое решение
def some_f(n, a, b):
    lst = list(range(n+1))
    lst_neg = list(map(lambda x: x*-1, lst)) # map и lambda вместо цикла for
    lst_neg.remove(0)
    lst_neg = list(reversed(lst_neg))
    lst_new = lst_neg + lst
    res = lst_new[a-1] * lst_new[b-1]
    print(lst_new, res)

some_f(int(input('N = ')), int(input('a = ')), int(input('b = ')))

# 4) Задача 1 из третьего дз. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Старое решение
elements = input('Введите несколько чисел: ').split()
elem_list = list(elements)[1::2]
print (elem_list)
new_list = [int(i) for i in elem_list]
print (new_list)
print ('Ответ:', sum(new_list))

# Новое решение
elements = list(input('Введите несколько чисел: ').split())
print(elements)
res = 0
for i, item in enumerate(elements): # enumerate
    item = int(item)
    if i % 2 == 1:
        res += item
print(res)

# Ещё одно решение этой задачи
elements = list(input('Введите несколько чисел: ').split())
lst = list(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 1, enumerate(elements)))) # lambda, filter, map
print (lst)
new_lst = list(map(lambda x: int(x), lst))
print(sum(new_lst))

# Ещё одно решение этой же задачи. Оно большое и вряд ли оптимизированное, но я попыталась его выполнить ради использования zip,
# тк больше применению zip не нашла в других задачах.

elements = list(input('Введите несколько чисел: ').split())
print(elements)
res = 0
elements = [int(i) for i in elements] # Создала список из числовых элементов
print(elements)
lst = list(enumerate(elements)) # Создала список с кортежами
print(lst)
for i in lst:
    if i[0] % 2 == 0:
        lst.remove(i) # Удалила те кортежи, в которых первый элемент (то есть индекс элемента в изначальном списке) чётный
print(lst)
justtt = list(zip(*lst)) # Сложила индексы в одном кортеже, а элементы - в другом
print(justtt)
for item in justtt:
    if item[0] % 2 == 1 and item[1] % 2 == 1:
        justtt.remove(item) # Удалила кортежи с нечётными индексами, тк они нам больше не нужны
print(justtt)

def crazy_sum(param): # Функция суммирования элементов из кортежа
    s = 0
    for item in param:
        s += item
    return s
print(crazy_sum(*justtt))
