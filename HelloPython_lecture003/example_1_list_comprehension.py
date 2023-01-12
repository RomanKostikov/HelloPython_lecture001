"""Doc."""
# structure variante
# [exp for item in iterable]
# [exp for item in iterable(if conditional)]
# [exp < if conditional > for item in iterable(ifconditional)]

# first variente

# list = []

# for i in range(1, 101):
#     # if (i % 2 == 0):
#     list.append(i)

# print(list)

# оптимизированный код
# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)

# дополненный код


# def f(x):
#     return x**3


# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# пример из теории:
# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# первый вариант решения задачи
# path = 'c://Users//roman//Desktop//Work for IT//GeekBrains//'\
#     'lecture//Python//Python_code_lecture//HelloPython_lecture003//file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# второй вариант решения через lamda

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
res = where(lambda e: not e % 2, res)
res = list(select(lambda e: (e, e**2), res))
print(res)

# третий вариант решения(lambda+map+filter)
# data = '1 2 3 5 8 15 23 38'.split()
# res = list(map(int, data))
# res = list(filter(lambda e: not e % 2, res))
# res = list(map(lambda e: (e, e**2), res))
# print(res)
