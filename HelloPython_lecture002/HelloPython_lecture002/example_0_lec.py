"""Doc."""
# первый вариант записи данных
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)  # разделителей не будет
# data.write('\nLINE 21\n')
# data.write('LINE 32\n')
# data.close()

# второй вариант записи данных(разрыв происходит автоматически, без data.close)
# with open('file.txt', 'a') as data:
#     data.write('line 11111\n')
#     data.write('line 22222\n')

# считываем файл txt
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
