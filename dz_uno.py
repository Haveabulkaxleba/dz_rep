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
