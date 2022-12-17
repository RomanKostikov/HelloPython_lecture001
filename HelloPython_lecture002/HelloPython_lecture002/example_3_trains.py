"""Doc."""
import os
os.system('cls')
# Кортеж – это неизменяемый “список”
# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)  # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)  # ('red', 'green', 'blue')

# mini example
a = (3, 4)
b = (3,)  # минимально необходимое для определения кортежа
print(b)
print(a)
print(a[0])  # обратились к конкретному элементу кортежа
print(a[-1])  # вызов последнего элемента кортежа

# перебор кортежей при помощи циклов
# t = tuple(['red', 'green', 'blue'])
# print(t[0])  # red
# print(t[2])  # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2])  # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e)  # red green blue
# t[0] = 'black'  # TypeError: 'tuple' object does not support
# # item assignment

# дополнение: распаковка кортежа в отдельные переменные
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue
