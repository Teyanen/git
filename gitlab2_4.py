print('Вводите элементы, нажимайте enter')
print('для окончания ввода нажмите enter')
a = int(input('> '))
my_list = []
while True:
    try:
        my_list.append(a)
        a = int(input('> '))
    except:
        break

print('В списке {} элементов'.format(len(my_list)))

my_list.pop(0)
my_list.pop(0)

k = 0
while k < 2:
    n = input("Введите число для добавления в конец списка: ")
    my_list.append(int(n))
    k += 1

print(my_list)