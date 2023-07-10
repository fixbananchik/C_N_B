def change_name(gamer, game):
    gamer.new_name()

def change_password(gamer, game):
    gamer.new_password()

from ..standart_rules import rules

def create_game(gamer, game):
    buf_name = input('Название игры: ')
    buf_pass = input('Введите пароль игры: ')
    #todo импортировать
    return Game(buf_name, 0, gamer, rules, buf_pass)

def connect_game(gamer, game):
    from ..soure import find_game
    finded_game = find_game()
    if finded_game:
        finded_game.users.append(gamer)
    else:
        print('Игра не найдена')



actions = {1: change_name, 2: change_password, 3:create_game}

def menu_actions(param, gamer, game):
    actions[param](gamer, game)
    
