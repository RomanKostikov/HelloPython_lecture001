"""Doc."""
# Управляющие конструкции:
# if, if-else

# простой пример
# if condition:
#  # operator 1
#  # operator 2
#  # ...
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # ...
#  # operator n + m

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# простой пример с elif
# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
