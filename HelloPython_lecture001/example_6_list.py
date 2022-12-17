"""Doc."""
# Списки: введение
# list = list
# 1 часть
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)  # приведение типа range к типу list
# print(type(numbers))

# numbers[0] = 10
# print(f'{len(numbers)} len')  # подсчет элементов
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]


# 2 часть
colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')  # del colors[0] # удалить элемент
