wins = int(input("Введите кол-во побед "))
loses = int(input("Введите кол-во поражений "))
draws = input("Введите кол-во ")




class Gamer:
    def __init__(self, wins, loses, draws):
        self.wins = wins
        self.loses = loses
        self.draws = draws