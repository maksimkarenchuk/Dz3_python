# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



# a = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(a)):
#     if i % 2 != 0:
#         sum += a[i]
# print(f"Сумма чисел на нечетных позициях: {sum}")


# n = int(input('Введите длину списка: '))
# list = []
# sum = 0
# for _ in range(n):
#     number = int(input())
#     list.append(number)
# for i in range(1, n, 2):
#     sum += list[i]
# print(f'Сумма чисел на нечетных позициях: {sum}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# n = int(input('Введите длинну списка: '))
# list = []
# for _ in range(n):
#     num = int(input())
#     list.append(num)
# new_list = []
# for i in range((n-1) // 2 + 1):
#     num1 = list[i]
#     num2 = list[n - i -1]
#     new_list.append(num1*num2)
# print(new_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.


# n = int(input('Введите длинну списка: '))
# list = []
# for _ in range(n):
#     num = float(input())
#     list.append(num)
# min = 1
# max = 0
# for i in list:
#     drob = str(i).split('.')[1]
#     if float('0.' + drob) > max
#         max = float('0.' + drob)
#     elif float('0.'+ drob) < min
#         min = float('0.' + drob)
# print(max-min)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a = int(input('Введите число: '))
# b = ''
# while a != 0:
#    b = str(a % 2) + b
#    a //= 2
# print(f'Bin = {b}')



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# k = int(input())
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# for idx in range(k + 2, k * 2 + 1):
#     some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
# for idx in range(k, -1, -1):
#     some_list[idx] = some_list[idx + 2] - some_list[idx + 1]
# print(some_list)
