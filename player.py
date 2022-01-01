from helpers import *
from attacks import Attack, createAttack

class Player:
    def __init__(self, name, hp, ac, attacks):
        self.id = genpId()
        self.name = name
        self.hp = hp
        self.ac = ac
        if (attacks != None):
            self.attacks = attacks
        else:
            self.attacks = [Attack("def", 1)]
        self.dead = False

    def attack(self,target,attackID):
        """kallar á takedamage() með þægilegra syntax"""
        takeDamage(target,self.attacks[attackID-1])

    def addAttack(self,attack):
        self.attacks.append(attack)

    def delAttack(self,attack):
        test = []
        test.remove(attack)

    def toString(self):
        nAtt = 1
        print("*****************************")
        print("ID:      ",self.id)
        print("Name:    ",self.name)
        print("Health:  ",self.hp)
        print("Armor:   ",self.ac)
        print("Dead:    ",self.dead)
        print("Attacks: ")
        for i in self.attacks:
            print(f'\t{nAtt}. {i.name}')
            nAtt+=1
        print("*****************************")

def createPlayer():
    print("~~~ create player ~~~")
    name = input("Player name: ")
    print("integer that represents health, can't be negative")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    hp = input("Player health: ")
    print("integer that represents armor, can't be negative")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ac = input("Player armor: ")
    print("integer that represents number of attacks")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    nAttacks = int(input("Number of attacks: "))
    attacks = []
    for i in range(nAttacks):
        existing = input("Does attack already exist (y/n): ")
        if existing == "n":
            attacks.append(createAttack())
        else:
            attacks.append(selectAttacks())

pId = 0
def genpId():
    global pId
    rId = "p"+str(f'{pId:03d}')
    pId+=1
    return(rId)

# testing