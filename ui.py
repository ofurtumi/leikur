from world import World
from helpers import *
from attacks import createAttack
from player import createPlayer
# from enemy import createEnemy

world = World()

def listMenu():
    clear()
    print(f'[1] list attacks')
    print(f'[2] list players')
    print(f'[3] list enemies')
    print(f'[4] list all')
    print(f'[5] go back')

    toList = int(input("choose list: "))

    match toList:
        case 1:
            clear()
            print("showing all attacks")
            for a in world.attacks:
                print(f'[{world.attacks.index(a)}] {a.name}')
            selectListItem(world.attacks)

        case 2:
            clear()
            print("showing all players")
            for a in world.players:
                print(f'[{world.players.index(a)}] {a.name}')
            selectListItem(world.players)
        
        case 3:
            clear()
            print("showing all enemies")
            for a in world.enemies:
                print(f'[{world.enemies.index(a)}] {a.name}')
            selectListItem(world.enemies)

        case 4:
            clear()
            print("showing everything")
            print("~~~ attacks ~~~")
            for a in world.attacks:
                print(f'[{world.attacks.index(a)}] {a.name}')
            print("~~~ players ~~~")
            for p in world.players:
                print(f'[{world.players.index(p)}] {p.name}')
            print("~~~ enemies ~~~")
            for e in world.enemies:
                print(f'[{world.enemies.index(e)}] {e.name}')
            input("press enter to go back")
            showMenu()
        
        case 5:
            showMenu()


def showMenu():
    clear()
    print(f'[1] create attack')
    print(f'[2] create player')
    print(f'[3] create enemy')
    print(f'[4] list creations')

    menuInput = int(input("choose menu: "))
    
    match menuInput:
        case 1:
            print("create attack")
            createdAttack = createAttack()
            createdAttack.toString()
            saveAttack = input("save (y,n): ")
            if saveAttack == "y" or saveAttack == "":
                world.newAttack(createdAttack)
                clear()
                print("saved, going to menu")
                showMenu()
            else:
                clear()
                print("not saved, going to menu")
                showMenu()

        
        case 2:
            print("create player")
            createdPlayer = createPlayer()
            clear()
            createdPlayer.toString()
            print()
            saveAttack = input("save (y,n): ")
            if saveAttack == "y":
                world.newPlayer(createdPlayer)
                print("saved, going to showMenu")
                showMenu()
            else:
                clear()
                print("not saved, going to showMenu")
                showMenu()

        case 3:
            print("create enemy")

        case 4:
            listMenu()

        case _:
            print("invalid selection, try again")
            showMenu()

def selectListItem(al):
    print("use id to get item overview or go back by using 'e'")
    selection = input("select: ")
    clear()
    if selection != 'e':
        selection = int(selection)
        al[selection].toString()
        input("press enter to go back")
        showMenu()
    else:
        showMenu()