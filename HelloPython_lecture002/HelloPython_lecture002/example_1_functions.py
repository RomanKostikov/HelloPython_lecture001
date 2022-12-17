"""Doc."""
import os
os.system('cls')
# Это фрагмент программы, используемый
# многократно
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return
# пример
# вызов ранее написанной функции + укоротилии ее название
# import example_7_function._lec001 as e7f

# print(e7f.f(1))

# пример 1 из презентации(значения по умолчанию для функции)


# def new_string(symbol, count):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # TypeError missing 1 required ...

# пример 2 из презентации(возможность передачи неограниченного
# колличества аргументов)

# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12

# пример 3


def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...
