my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;' \
            'Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;' \
            'Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;' \
            'Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;' \
            '21 год;Студент 2 курса'
my_list = my_string.split(';')

m = 0
while m < len(my_list):
    my_list[m] = my_list[m].replace('_', '')
    m += 1

print("%20s%20s%20s" % (my_list[0], my_list[1], my_list[2]))

k = 0
while k < len(my_list):
    if 'Петров' in my_list[k]:
        print("%20s%20s%20s" % (my_list[k], my_list[k+2], my_list[k+1]))
k += 1