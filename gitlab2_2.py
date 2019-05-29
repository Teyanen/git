my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
my_list = my_string.split(';')

k = 0
while k < len(my_list):
    my_list[k] = my_list[k].replace('_', '')
    k += 1

print("%20s%20s%20s" % (my_list[0] + my_list[1] + my_list[2], my_list[4], my_list[3]))
print("%20s%20s%20s" % (my_list[5] + ' ' + my_list[6] + ' ' + my_list[7], my_list[9], my_list[8]))
print("%20s%20s%20s" % (my_list[10] + ' ' + my_list[11] + ' ' + my_list[12], my_list[14], my_list[13]))