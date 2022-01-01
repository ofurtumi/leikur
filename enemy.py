from helpers import *
from attacks import Attack

class Enemy:
    def __init__(self, name, hp, ac, attacks):
        self.id = geneId()
        self.name = name
        self.hp = hp
        self.ac = ac
        if (attacks != None):
            self.attacks = attacks
        else:
            self.attacks=[Attack("def", 1)]
        self.attacks = attacks
        self.dead = False

    def attack(self,target,attackID):
        """kallar á takedamage() með þægilegra syntax"""
        takeDamage(target,self.attacks[attackID-1])

    def toString(self):
        nAtt = 1
        print("*****************************")
        print("ID:      ",self.id)
        print("Enemy:   ",self.name)
        print("Health:  ",self.hp)
        print("Armor:   ",self.ac)
        print("Dead:    ",self.dead)
        print("Attacks: ")
        for i in self.attacks:
            print(f'\t{nAtt}. {i.name}')
            nAtt+=1
        print("*****************************")

eId = 0
def geneId():
    global eId
    rId = "p"+str(f'{eId:03d}')
    eId+=1
    return(rId)

# def playerGen():
