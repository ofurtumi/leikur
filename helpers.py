import os
import random
import keyboard

clear = lambda: os.system('clear')


def d6():
    return random.randint(1, 6)

def d20():
    return random.randint(1, 20)

def d100():
    return random.randint(1, 100)

def takeDamage(self, attack):
        """function til þess að láta entities taka damage,
        skilar false ef entity er lifandi og true ef þap deyr
        
        self er það entity sem á að taka damage,
        damage er int sem á að draga frá heildar hp"""
        hit = d20()
        if (hit+attack.bonus >= self.ac):
            print("hit",hit)
            if self.hp > attack.pow:
                self.hp -= attack.pow
                print(self.name, " hp: ", self.hp)
                return False
            else:
                self.hp = 0
                self.dead = True

        else:
            print("miss",hit)

        if (self.dead):
            print(self.name + " is dead")

def multiAttack(attack, target, n):
    """kallar á takedamage n oft eða þangað til að target er dautt"""
    counter = 0
    for i in range(n):
        takeDamage(target,attack)
        counter = i+1
        if(target.dead):
            break
    print("attacked", counter, "times")

# def selectAttacks():
#     print("choose attack by id")
#     for i in range(len(allAttacks)):
#         print(f'[{i}] {allAttacks[i].name}')
#     chosenAttack = input("attack id: ")
#     return(allAttacks[chosenAttack])
