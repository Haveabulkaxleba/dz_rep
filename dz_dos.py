# Задание 1 Программа, которая принимает на вход вещественное число и показывает сумму его цифр.
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

# # Задание 2 Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# number = int(input('Введите число:'))
mult = 1
k = 0
lst = []
while k < number:
    k += 1
    mult *= k
    lst.append(mult)
print (lst)

# # Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# # округлённую до трёх знаков после точки.
# n = 6
# lst = [(1+1/n)**n for i in range(n+1)]

# print (lst)

# #  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на позициях a и b.
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
# Задание 5 Реализуйте алгоритм перемешивания списка.
import random

somelist = [1, 2, 3, 4, 5, 6, 7]
shuffled_list = []
items = len(somelist)
count = 0
while count != items:
    k = random.choice (somelist)
    somelist.remove(k)
    count += 1
    if k not in somelist:
        shuffled_list.append (k)
    else:
        break
print(shuffled_list)