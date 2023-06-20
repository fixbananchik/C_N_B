round = int(input("Введите раунд "))
users = int(input("Введите кол-во игроков "))
password = input("Введите пароль ")

class Game:
    def __init__(self, round, users, rules, password):
        self.round = round
        self.users = [users]
        self.rules = rules
        self.password = password

    def start(self):
        pass
    def end(self):
        pass

