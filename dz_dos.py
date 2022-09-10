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

# Задание 2 Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input('Введите число:'))
mult = 1
k = 0
lst = []
while k < number:
    k += 1
    mult *= k
    lst.append(mult)
print (lst)