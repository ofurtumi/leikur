from helpers import *
from attacks import Attack, createAttack, attackGen
from enemy import Enemy
from player import Player, createPlayer
from ui import *

def testAll():
    testAttack = Attack("test",1)
    testAttack.toString()

    testPlayer = Player("tumi",9999,25,[Attack("ultra_blast",9001,20,"divine")])
    testPlayer.toString()
    testPlayer.attacks[0].toString()

    testEnemy = Enemy("slime", 10, 5, [Attack("slime_attack",5,1)])
    testEnemy.toString()
    testEnemy.attacks[0].toString()


def play():
    aG = attackGen()
    for i in aG:
        world.newAttack(i)
    showMenu()

play()