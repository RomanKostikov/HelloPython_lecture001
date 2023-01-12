"""Doc."""
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#                  ↓
#              [ 2, 4 ]
# Нельзя пройтись дважды

# элементарный пример

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

# третий вариант решения(lambda+map+filter)

data = '1 2 3 5 8 15 23 38'.split()
res = list(map(int, data))
res = list(filter(lambda e: not e % 2, res))
res = list(map(lambda e: (e, e**2), res))
print(res)
