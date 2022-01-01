class World:
    def __init__(self):
        self.attacks = []
        self.players = []
        self.enemies = []

    def newAttack(self, attack):
        self.attacks.append(attack)

    def newPlayer(self, player):
        self.players.append(player)

    def newEnemy(self, enemy):
        self.enemies.append(enemy)

    