#Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
elements = input('Введите несколько чисел: ').split()
elem_list = list(elements)[1::2]
print (elem_list)
new_list = [int(i) for i in elem_list]
print (new_list)
print ('Ответ:', sum(new_list))

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
nums = [int(item) for item in input ('Введите несколько чисел: ').split()]
nums_lst = list(nums)
new_list = []
new = []
n = len(nums_lst)
i = 0
for item in nums_lst:
    mult = nums_lst[i] * nums_lst[n-1]
    new_list.append(mult)
    i += 1
    n -= 1
print (new_list)
for b in new_list:
    if b not in new:
        new.append(b)
print (new)

#Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
numbers = [1.1, 1.2, 3.1, 5, 10.01]
tmp = []
for i in numbers:
    a = i - int(i)
    tmp.append(round(a, 2))
    for item in tmp:
        if item == 0:
            tmp.remove(item)
        else:
            num_max = max(tmp)
            num_min = min(tmp)
            answer = num_max - num_min
print (tmp)
print ('Ответ:', answer)

#xЗадача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('Введите число: '))
answer = ''
while number > 0:
    help_string = str(number % 2)
    answer = help_string + answer
    number = number // 2
print (answer)

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = 8
f1 = 1
f2 = 1
lst = [1, 1]
for k in range (2, n):
    f1, f2 = f2, f1+f2
    lst.append(f2)
f11 = 0
f12 = 1
lst2 = [0, 1]
for i in range (-n+2, 1):
    f11, f12 = f12, f11 - f12
    lst2.append(f12)
new = list(reversed(lst2))
print(new + lst)

