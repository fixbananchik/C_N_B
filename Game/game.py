round = int(input("Введите раунд "))
users = int(input("Введите кол-во игроков "))
password = input("Введите пароль ")

class Game:
    def __init__(self, name, round, users, rules, password):
        self.name = name
        self.round = round
        self.users = [users]
        self.rules = rules
        self.password = password

    def start(self):
        pass
    def end(self):
        pass

