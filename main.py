from soure.game_menu import game_menu
from Gamer import Gamer
from soure import mms
from Game import Game
from soure import find_person
from soure import menu_actions

in_menu = True

person = None #текущий игрок
game = None

persons = []
games = []

while in_menu:
    param = None
    param = mms(person)

    if not param:
        param = int(input())
    if param == 1:

        buffer_name = input('Введите имя: ')
        buffer_password = input('Введите пароль: ')
        persons.append(Gamer(0,0,0,buffer_name, buffer_password))

    elif param == 2:
        #вход
        if not person:
            person = find_person(persons)

        if person:
            param = game_menu()
            if param == 5:
                person = None
            else:
                new_game = menu_actions(param, person, game)
                if new_game:
                    games.append(new_game)

        else:
            print('Пользователь не найден')

    elif param == 3:
        game = False
    else:
        print('Неверный ввод')