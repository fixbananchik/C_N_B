
from Gamer import Gamer
from soure import mms

in_menu = True

person = None #текущий игрок
game = None

persons = []
games = []

while in_menu:
    mms()
    param = int(input())
    1+1

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
                    if new_param == 1:
                        pass
                    elif new_param == 2:
                        person.new_password() 
                        1+1
                    elif new_param == 3:
                        pass
                    elif new_param == 4:
                        pass
                    else:
                        pass

                else:
                    print('Неверный пароль')
                finded = True
        if finded == False:
            print('Пользователь не найден')

    elif param == 3:
        game = False
    else:
        print('Неверный ввод')