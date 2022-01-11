print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|________
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=._________________|_______
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

mountain_=input("You're at the foot of a mountain.Do you want to climb it?Type'Yes'or'No'")
mountain=mountain_.lower()
if mountain=="yes":
   water_=input("You find a river.There is an island in the middle of  it.Type'swim'to swim across.Type 'wait'to wait for a boat.")
   water=water_.lower()
   if  water=="wait":
     doors_colour=input("You arrive at the island unharmed.There is a house with 3 doors.One is violet, one is yellow, one is blue.Which one do you choose?")
     doors=doors_colour.lower()
     if doors=="violet":
       print("You entered a room of VAMPIRES!!!.GAME OVER *_*.")
     elif doors=="yellow":
       print("It's a free fall good luck finding the bottom.GAME OVER!!!.")
     else:
       print("You found the treasure!!! Yayy.")  
   else:
    print("Oh noo...the speed of the river was too much for you.GAME OVER!!!")
else:
  print("Oops!A bear was just following you \"_\".GAME OVER!!!")

 

  
