from Gamer import Gamer
from soure import mms

in_menu = True

person = None
game = None

persons = []
games = []

while in_menu:
    mms()
    param = int(input())

    if param == 1:

        buffer_name = input('Введите имя: ')
        buffer_password = input('Введите пароль: ')
        person = Gamer(0,0,0,buffer_name, buffer_password)
        persons.append(person)

    elif param == 2:
        buffer_name = input('Введите имя: ')
        buffer_password = input('Введите пароль: ')

        finded = False

        for p in persons:
            if p.name == buffer_name:
                if p.password == buffer_password:
                    print('Успешный вход')
                    person = p
                    new_param = int(input())
                else:
                    print('Неверный пароль')
                finded = True
        if finded == False:
            print('Пользователь не найден')

    elif param == 3:
        game = False
    else:
        print('Неверный ввод')