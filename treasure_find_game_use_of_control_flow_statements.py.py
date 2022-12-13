print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇

print("Welcome to Treasure Island. Your mission is to find the treasure. ")
user_choose=input("Please Enter left and right: ")
convert=user_choose.lower()
if convert=='right':
    print("Fall into a Hole Game Over !")
elif convert=="left":
    swim_wait=input("Do you want to swim or boat:  ")
    convert_swim_wait=swim_wait.lower()
    if convert_swim_wait=="swim":
        print("You Attacked by Trout Game Over !")
    elif convert_swim_wait=='boat':
        choose_door=input("Finally You reached ! Please enter door name Yellow, Blue, Red : ")
        if choose_door.lower()=="yellow":
            print("You Found the Treaure")
        else:
            print("You killed by the shark Game Over !")
    else:
        print("You enter wrong option please start it again")
else:
    print("You enter wrong option please start it again")

    
