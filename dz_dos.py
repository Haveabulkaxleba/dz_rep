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