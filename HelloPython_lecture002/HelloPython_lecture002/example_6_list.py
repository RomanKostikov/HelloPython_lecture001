"""Doc."""
import os
os.system('cls')
# Углубление в списки
# первая особенность(замена значений в списке)
# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123  # меняется значение в первом и втором списке
# list2[1] = 333  # меняется значение в первом и втором списке
# print()

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# вторая особенность
list1 = [1, 2, 3, 4, 5]

# print(len(list1))  # удаление последнего элемента списка
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.pop(2))  # удаление конкретного элемента списка
# print(list1)

print(list1.insert(2, 11))  # добавлнеие на нужную поз
print(list1)

print(list1.append(11))  # добавлнеие в конец
print(list1)
