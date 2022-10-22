#1 Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
# a = float(input('Введите вещественное число: '))
# n = int(input('Введите точность: '))
n = str(n)
n = n.split('.')



# print(round(a, n))
# print(f'{a:.{n}f}')



#2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input('Введите число: '))
# factors = []
# d = 2
# m = n
# while d * d <= n:
#     if n % d == 0:
#         factors.append(d)
#         n//=d
#     else:
#         d += 1
# factors.append(n)
# print('{} = {}' .format(m, factors))


#3  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# numbers = [1, 2, 2, 3, 3, 4, 5, 6]

# some_list = []
# new_list = set(numbers)
# for numbers in some_list:
#     some_list.append(numbers)
# print(new_list)


# new_list = list(set(numbers))
# print(new_list)

