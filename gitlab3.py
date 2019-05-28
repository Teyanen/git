import sys
import os


def exit():
    m = input('Вы хотите продолжить? (y/n)')
    if m == 'y':
        menu()
    else:
        sys.exit()


def count_files():
    di = input('Введите адрес директории: ')
    print('Файлов в директории:',len([name for name in os.listdir(di) if os.path.isfile(os.path.join(di, name))]))
    exit()


def show_products():
    k = 0
    file = open(b'C:\Users\drlol\PycharmProjects\laboratornaya_3\products.txt', 'r')
    n_list = file.read().splitlines()
    for elem in n_list:
        n_list[k] = elem.split(';')
        k += 1
    header = n_list.pop(0)
    print('%3s%20s%10s%10s' % (header[0], header[1], header[2], header[3]))
    n_list.sort(key=lambda x: x[1])
    for elem in n_list:
        print('%3s%20s%10s%10s' % (elem[0], elem[1], elem[2], elem[3]))
    exit()


def increase_cost():
    k = 0
    file = open(b'C:\Users\drlol\PycharmProjects\laboratornaya_3\products.txt', 'r')
    n_list = file.read().splitlines()
    for elem in n_list:
        n_list[k] = elem.split(';')
        k += 1
    header = n_list.pop(0)
    print('%3s%20s%10s%10s' % (header[0], header[1], header[2], header[3]))
    n_list.sort(key=lambda x: x[1])
    for elem in n_list:
        print('%3s%20s%10s%10s' % (elem[0], elem[1], elem[2], elem[3]))
    print('Введите номер товара, количество которого хотите изменить:')
    num = input('>>')
    print('Введите изменение количества:')
    quantity = input('>>')
    for elem in n_list:
        if elem[0] == num:
            print('Товар: {}'.format(elem))
            elem[3] = int(elem[3]) + int(quantity)
            print('Измененный товар: {}'.format(elem))
    i = input('Сохранить измененный список товаров в файл? (y/n)')
    if i == 'y':
        f = open(b'C:\Users\drlol\PycharmProjects\laboratornaya_3\products_modified.txt', 'w')
        f.write(str(header) + '\n')
        for elem in n_list:
            f.write(str(elem) + '\n')
        print('Файл записан!')
        f.close()
        exit()
    else:
        exit()


def menu():
    print('0 - Выход\n1 - Посчитать файлы в директории\n2 - Вывод информации о товарах, сортированных по значению'
          '\n3 - Изменение количества товаров указанных номеров')
    m = input('>>')
    if m == '0':
        sys.exit()
    if m == '1':
        count_files()
    if m == '2':
        show_products()
    if m == '3':
        increase_cost()


menu()