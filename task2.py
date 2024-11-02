# Напиши функцию aggregate,
# которая принимает список чисел и функцию operation,
# выполняющую определённую операцию над парой чисел,
# а также начальное значение.
# Функция должна применить operation ко всем
# элементам списка и вернуть результат.

# Пример:
# [1, 2, 3, 4, 5]
# Передаваемая функция: функция сложения
# результат : 15

# [1, 2, 3, 4, 5]
# Передаваемая функция: функция умножения
# результат : 120

import math

_lst = [1, 2, 3, 4, 5]
lst1 = 0
def aggregate(func: callable, _lst: int):
    lst1 = func(_lst)
    return lst1

#operations = sum
operations = math.prod
res = aggregate(operations, _lst)
print(res)


