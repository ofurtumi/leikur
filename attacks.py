from helpers import clear

class Attack:
    def __init__(self, name, pow, bonus, elem="normal"):
        self.id = genaId()
        self.name = name
        self.pow = pow
        self.bonus = bonus
        self.elem = elem

    def toString(self):
        print("*****************************")
        print("ID:     ",self.id)
        print("Attack: ",self.name)
        print("Power:  ",self.pow)
        print("Bonus:  ",self.bonus)
        print("Element:",self.elem)
        print("*****************************")

def createAttack():
    clear()
    print("~~~ create attack ~~~")
    name = input("attack name: ")
    clear()
    print("integer that represents damage, negative for healing")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    power = input("attack power: ")
    clear()
    print("integer that adds to hit calculation, can be negative")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    bonus = input("attack bonus: ")
    clear()
    print("elemental type of attack, can be empty")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    element = input("attack type: ")
    if element != "":
        return Attack(name,power,bonus,element)
    else:
        return Attack(name,power,bonus)
    clear()

aId = 0
def genaId():
    global aId
    rId = "a"+str(f'{aId:03d}')
    aId+=1
    return(rId)

def attackGen():
    attacks = [
        Attack("default",0,0),
        Attack("bone_club",5,2),
        Attack("skull_bash",7,1),
        Attack("slime_slap",3,5,"acid"),
        Attack("slime_shot",10,0,"acid")
    ]
    return attacks