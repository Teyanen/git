str1 = 'Погиб поэт!- невольник чести - Пал, оклеветанный молвой, С свинцом в груди и жаждой мести, Поникнув гордой головой!..'

# Больше 5 символов, разделитель - пробел
str2 = str1.split()

k = 0
while k < len(str2):
    str2[k] = str2[k].replace(',', '')
    str2[k] = str2[k].replace('.', '')
    str2[k] = str2[k].replace('—', '')
    k += 1

str1 = ''
for elem in str2:
    if len(elem) > 5:
        str1 += elem + ' '

print(str1)