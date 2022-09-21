# Предложить улучшения кода для уже решённых задач (4 задачи из любых семинаров, кроме первого):
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

# Задача 1 из второго дз. Программа, которая принимает на вход вещественное число и показывает сумму его цифр.
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