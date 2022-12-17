"""Doc."""
import os
os.system('cls')
# Неупорядоченная совокупность элементов
# пример 1 из презентации
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # set
# print(type(b))  # set

# пример 2 из презентации
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b))  # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}

# пример 3 из презентации(базовые api(appy) для работы с множеством)
# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# # print(type(colors))  # узнали какой тип данных
# # exit()
# colors.add('red')  # добавили во множество
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue','gray'}
# colors.remove('red')  # удалили из множества
# print(colors)  # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')  # ok # удалили из множества без ошибки
# print(colors)  # {'green', 'blue','gray'}
# colors.clear()  # { } отчистили множество
# print(colors)  # set()

# пример 4 из презентации(операции со множествами(пересечения и т д))
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)  # i = {8, 2, 5}
# dl = a.difference(b)  # dl = {1, 3}
# dr = b.difference(a)  # dr = {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# {1, 21, 3, 13}

# пример 5 из презентации(неизменяемое множество)
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})
