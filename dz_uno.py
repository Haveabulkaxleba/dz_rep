# Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
number = int(input ("Введите номер дня недели: "))
if 0 < number < 6:
    print ("Будний день :(")
elif 6 <= number <= 7:
    print ("Выходной :)")
else:
    print ("Нет дня недели с таким номером")
    
    
    
# Программа, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
coordinate_x = int(input("x = "))
coordinate_y = int(input ("y = "))
if coordinate_x > 0 and coordinate_y > 0:
    print ("Точка - в 1 четверти")
elif coordinate_x < 0 and coordinate_y > 0:
    print ("Точка - во 2 четверти")
elif coordinate_x < 0 and coordinate_y < 0:
    print ("Точка - в 3 четверти")
elif coordinate_x > 0 and coordinate_y < 0:
    print ("Точка - в 4 четверти")
elif coordinate_x == 0 and (coordinate_y > 0 or coordinate_y < 0):
    print ("Точка - на оси y")
elif (coordinate_x > 0 or coordinate_x < 0) and coordinate_y == 0:
    print ("Точка - на оси x")
else:
    print ("Точка -это место пересечения осей x и y")


# Программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
num = int (input("Введите номер четверти: "))
if num == 1:
    print ("У точки в четверти", num, "координаты x и y больше нуля")
elif num == 2:
    print ("У точки в четвети", num, "координаты x и y меньше и больше нуля соответственно")
elif num == 3:
    print ("У точки в четвети", num, "координаты x и y меньше нуля")
elif num == 4:
    print ("У точки в четвети", num, "координаты x и y больше и меньше нуля соответственно")

# Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def input_coordinates1 ():
    a_x = int(input("Введите координату X точки A: "))
    a_y = int(input("Введите координату Y точки A: "))
    a_full = [a_x, a_y]
    return a_full

def input_coordinates2 ():
    b_x = int(input("Введите координату X точки B: "))
    b_y = int(input("Введите координату Y точки B: "))
    b_full = [b_x, b_y]
    return b_full

def calculate_distance (a, b):
    dist = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5
    return dist
aaa = input_coordinates1()
bbb = input_coordinates2()
print (aaa)
print (bbb)
print ("Расстояние между точками A и B =", round(calculate_distance(aaa, bbb), 3))