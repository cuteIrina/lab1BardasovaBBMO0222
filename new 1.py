# Часть 1
import random
import array as arr
#Код реализован на Python. Функция заполнения массива случайными числами
#Для решения задачи использовала цикл for
def func(length, min_value, max_value):
    array = [] #Создаем пустой массив
    for _ in range(length):
        value = random.randint(min_value, max_value)
        array.append(value) #Добавляем число в массив
    return array
#C помощью функции random.randint() создали случайное число в заданном диапазоне. 

def print_array(array):
    for value in array:
        print(value, end=' ')
    print("Это наш сгенерированный массив")

length = int(input("Введите длину массива: ")) #Запрашивает у пользователя размер массива
min_value = int(input("Введите начало диапазона: ")) 
max_value = int(input("Введите конец диапазона: ")) 

#Далее выводим массив на экран с помощью функции print()

my_array = func(length, min_value, max_value)
print_array(my_array) #Выводит наш массив на экран