#поиск игрока

def find_game(games):
    buffer_name = input('Введите название игры: ')
    buffer_password = input('Введите пароль игры: ')
    
    for g in games:
        if g.name == buffer_name and g.password == buffer_password:
            return g
    return None