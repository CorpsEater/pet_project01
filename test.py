number = input("Введи номер телефона\n")
while True:
    if len(str(number)) == 11 and str(number)[0] in ('7','8'):
        print('Проверка успешная')
        break
    else:
        number = input(f'Кол-во символов: {len(str(number))}\nПервый символ: {str(number)[0]}\n\nНомер не корректный, повтори попытку\n')