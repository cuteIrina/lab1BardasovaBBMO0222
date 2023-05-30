# Часть 1
import random
import array as arr
#Код на python. Функция заполнения массива случайными числами
#Для заполнения массива случайными числами можно воспользоваться модулем random из стандартной библиотеки Python.
def func(length, min_value, max_value):
    array = []
    for _ in range(length):
        value = random.randint(min_value, max_value)
        array.append(value)
    return array


def print_array(array):
    for value in array:
        print(value, end=' ')
    print()

length = int(input("Введите длину массива: "))
min_value = int(input("Введите начало диапазона: "))
max_value = int(input("Введите конец диапазона: "))

my_array = func(length, min_value, max_value)
print_array(my_array)