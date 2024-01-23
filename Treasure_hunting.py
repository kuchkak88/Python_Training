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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
select = input('You\'re in the dark forest, filled with dangerous animals and you reached an crossroad. Type "left" or "right".\n').lower()
if select == "left":
  select2 = input('You are on the right path. You\'ve reached a river. Do you swim or wait? Type "swim" or "wait"\n ')
  if select2 == "wait":
    select3 = input('You made a right choice. You\'ve reached a house with three doors. One red, one blue and one yellow. Which door do you choose?\n').lower()
    if select3 == "red":
       print("You chose a room with a beast. Game over!")
    elif select3 == "blue":
       print("You chose a room with a lion and you're dead. Game over!")
    elif select3 == "yellow":
       print("Congratulations! You've found the treasure. You win!")
    else:
       print("You've chosen a door which does not exist. Game over.")
  else:
    print("You've entered a water with full of poisonous snakes and very deep swamps. You're dead. Gave over!")
else:
  print("It is a wrong turn. You've been beaten to death by a grizzly bear. Game over!")