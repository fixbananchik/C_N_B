#поиск игрока

def find_person(persons):
    buffer_name = input('Введите имя: ')
    buffer_password = input('Введите пароль: ')
    
    for p in persons:
        if p.name == buffer_name and p.password == buffer_password:
            return p
    return None