"""Doc."""
# Теория
# Идея: часто описывать функцию
# некогда и незачем
# Анонимные, lambda функции 1


# def sum1(x):
#     return x+22


# def mult2(x):
#     return x**3


# sum1(mult2(2))


# def sum3(x):
#     return x+242


# def mult4(x):
#     return x**5


# sum3(mult2(2))

# Анонимные, lambda функции 2
# def sum(x): return x+10
# def mult(x): return x**2


# sum(mult(2))
# def sum1(x): return x+22
# def mult2(x): return x**3


# sum1(mult2(2))
# def sum4(x): return x+242
# def mult4(x): return x**5


# sum3(mult2(2))

# Анонимные, lambda функции 3
# def sum(x): return x+10
# def mult(x): return x**2


# sum(mult(2))
# f(g(x))
# def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))


# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)

# практика на лекции
# 1.функция возводит число в квадрат(знакомство)


# def f(x):
#     x**2
# # print(type(f))


# g = f
# print(f(1))
# print(g(1))

# 2.функция возводит число в квадрат(продолжение)
# def f(x):
#     return x**2


# g = f
# # print(f(2))
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# 3. пример использования вложенных функций, как переменных(простой пример)
# def calc1(x):
#     return x+10


# print(calc1(10))

# 3. пример использования вложенных функций, как переменных(средний пример)
# одна и таже логика с одной переменной


# def calc2(x):
#     return x*10


# # print(calc2(10))


# def math(op, x):
#     print(op(x))


# math(calc2, 10)
# math(calc1, 10)

# 4. пример использования вложенных функций, как переменных(средний пример)
# одна и таже логика с двумя переменными


# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y  # тоже самое, что и выше

def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


calc(lambda x, y: x+y, 4, 5)
