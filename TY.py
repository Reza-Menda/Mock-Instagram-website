import math
import time
import random
import cmd
import textwrap
import sys
import os
    
        
### M = Market ###
### D = Dungeon ###
### C = Center ###
### P = Prison ###
### F = Forest ###
location = {    "D1" : "Sol Forest Dungeon D1" ,
                "F2" : "Paxy Forest F2",
                "M2" : "Ansyahr Market M2",
                "C2" : "Ansyahr city center C2",
                "P2" : "Paxy Prison P2",}
if location == ("F2"):
        encounter_chance = random.randrange(1,5)
        if encounter_chance == 4:
            encounter_monster()
elif location != ("F2"):
        encounter_chance = 0

### Option ###
path_chose = {  "A1" : "option 1",
                "A2" : "option 2",
                "A3" : "option 3"}
### Title ###
def title_screen_selections():

    option = input(" Do you want to play? (Play/Help/Quit) (1/2/3)")
    if option.lower() == ("1"):
        start_game()
    elif option.lower() == ("2"):
        help_menu()
    elif option.lower() == ("3") :
        SystemExit

    if option not in ("1" , "2" , "3"):
        print("Please choose a valid command")

def buffs():
    print("Arbalistic")

### Help menu ###
def help_menu():
    print("===== How To Play =====")
    print("Reply to do action, each action will trigger a scene for you to reacct upon.")
    print("HP starts at 100, if you reach 0 you die.")
    print("MP is mana point, used to do special attacks")
    Help_quit = input("Back to menu? (Yes/No) (1/2)")
    if Help_quit == ("1"):
        print(".")
        title_screen_selections()
    elif Help_quit == ("2"):
        print(".")
        help_menu()

### Combat ###
def health_Point():
    100
    lose_menu = input("You lose, try again? (Yes/no) (1/2)")
    if health_Point() == 0:
        lose_menu
    elif lose_menu == ("1"):
        title_screen_selections
    elif lose_menu == ("2"):
        SystemExit

### Mana ###
def mana_fruit():
    mana_up = input("You have found a mana fruit, do you wish to eat it? (Yes/no) (1/2)")
def mana_point():
    100
    Empty_mana = print("you are out of mana")
    if mana_point() == 0:
        Empty_mana
    if mana_fruit() == (1):
        print("You have eaten the Mana Fruit! (MP + 20)")
        mana_point() == mana_point() + 20
    elif mana_fruit() == (2):
        print("You didn't eat the fruit.")


def start_game():
    spawn_location = random.randrange(1, 2)

    if spawn_location == 1:
        print(".")
        map_position = (location.get("F2"))
        print(map_position)
        print("You open your eyes amongst the tall pine trees, the sound of an owl woke you up.")
        forest_path1 = random.randrange(1, 2)
        if forest_path1 == 1:
            print("You spotted a lake close by, do you...")
            forest_path1_lake = input("A. Approach the lake. B. Sit still. C. Avoid the lake (A/B/C)")
            if forest_path1_lake == ("A"):
                print("We are numbre one")
                forest_path1_lake1 = (forest_path1_lake + ("1"))
                print(forest_path1_lake1)
                print(location.get("F2"), forest_path1_lake1)
            elif forest_path1_lake == ("B"):
                print("We are numbre two")
                forest_path1_lake2 =(forest_path1_lake + ("2"))
                print((location.get("F2")),forest_path1_lake2)
                print(forest_path1_lake2)
            elif forest_path1_lake == ("C"):
                print("We are numbre tree")
                forest_path1_lake3 =(forest_path1_lake + ("3"))
                print((location.get("F2")),forest_path1_lake3)
                print(forest_path1_lake3)
        elif forest_path1 == 2:
            print("You spotted a cave nearby, do you...")
            forest_path1_cave = input("1. Approach the cave. 2. Avoid the cave. (A/B)")
            if forest_path1_cave == ("A"):
                print("you chose 1")
            elif forest_path1_cave == ("B"):
                print("you chose numbre 2")
            
    elif spawn_location == 2:
        print(".")
        map_position = (location.get("M2"))
        print (map_position)
        print("The blinding light of the night market opened your eyes wide, the noisy crowd kept you from falling asleep.")
        market_path1 = random.randrange(1, 2)
        if market_path1 == 1:
            print("wallet")
            market_path1_wallet = input()
            if market_path1_wallet == 1:
                print()
        elif market_path1 == 2:
            print("map")
            market_path1_map = input()
            if market_path1_map == 1:
                print()


### Player Location ###
    sv_location = print(map_position + )

title_screen_selections()