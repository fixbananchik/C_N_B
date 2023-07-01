
class Gamer:
    def __init__(self, wins, loses, draws, my_name, my_password):
        self.wins = wins
        self.loses = loses
        self.draws = draws
        self.name = my_name
        self.password = my_password

    def new_password(self):
        buffer_password = input("Введите новый пароль ")
        self.password = buffer_password
