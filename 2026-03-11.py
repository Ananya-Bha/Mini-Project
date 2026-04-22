import random
player = {
  "name": "",
  "health": 100,
  "max_health": 200,
  "max_armour": 200, 
  "armour": 0,
  "gold": 50,
  "damage": 5,
  "potions": [],
  "weapons": []
}

#Dictionary for damage output of weapons
weapons = {
  "Sword": 20,
  "Knife": 10, 
  "Stick": 7,
  "Club": 15
}

enemies = [
  {"name": "Orc", "health": 50, "damage": 7, "gold": 15},
  {"name": "Zombie", "health": 40, "damage": 15, "gold": 25},
  {"name": "Alien", "health": 60, "damage": 20, "gold": 40},
  {"name": "Skeleton", "health": 20, "damage": 7, "gold": 10}
]
battle_counter=0

#Handles potion drinking
def potion_drinking():
  if len(player["potions"])==0:
    print("-- No potions available --")
    return
  print("These are the potions that you have available:")
  print(player["potions"])
  #User can input a potion or "q" to move on (loop if they don't enter these options)
  potion_choice=input("Which potion would you like to use? (Or enter 'q' to quit)\n> ")
  while (potion_choice not in player["potion"]) or (potion_choice != "q"):
    print("Invalid Potion")
    potion_choice=input("Which potion would you like to use?\n> ")
  #If user entered q, do nothing, else if the user entered a potion, remove the potion and apply its effects
  #Health potion adds 25 health (up to max health), armor potion adds 25 armor
  if potion_choice =="q":
    return
  player["potions"].remove(potion_choice)
  if potion_choice == "health":
    player["health"]+=25
    if player["health"]>player["max_health"]:
      player["health"]=player["max_health"]
  elif potion_choice =="armour":
    player["armour"]+=25
    if player["armour"]>player["max_armour"]:
      player["armour"]=player["max_armour"]
  print(f"Your {potion_choice} has been updated.\n You now have {player[potion_choice]} {potion_choice}!")

#Handles attack enemy
# - Choose a weapon
# - Subtract the health of the enemy based off the weapon chosen
def attack_enemy(enemy):
  damage_output = player["damage"]
  if len(player["weapons"])==0:
    print("-- No weapons available --")
  else:  
    print("These are the weapons that you have available:")
    print(player["weapons"])
    #User can input a weapon or "f" for fists (loop if not either of these choices)
    weapon_choice=input("Which potion would you like to use? (Or enter 'f' for fists)\n> ")
    while (weapon_choice not in player["weapons"]) or (weapon_choice != "q"):
      print("Invalid weapon")
      weapon_choice=input("Which weapon would you like to use?\n> ")
    if weapon_choice=="f":
  #TODO - Finish weapon handling


# Fighting enemy:
# - Randomly select one of the enemies
# - Have a loop where the player than drink a potion/fight/run away
# - Enemy attacks the player
def fight_enemy():
  battle_counter += 1
  enemy = random.choice(enemies).copy()
  print(f" --- Battle {battle_counter}--- \n")
  print(f"The enemy that you will fight is - {enemy["name"]} - ")
  while player["health"]>0 and enemy["health"]>0 :
    #Enemy attacks the player first
    player["health"]-=enemy["damage"]
    print(f"The {enemy["name"]} has attacked you by {enemy["damage"]}!\n Your new health is {player["health"]}")
    if player["health"]<0:
      print("You have no health left!")
      break
    print(f" -- Options Available -- \n")
    print("1. Drink Potion")
    print("2. Fight")
    print("3. Run away")
    choice= input("What would you like to do: ")
    if choice=="1":
      potion_drinking()
    elif choice=="2":
      attack_enemy(enemy)
    elif choice=="3":
      return
    # - If enemy is less than 0, you won
      

      
        
      
        
        
          
          
        


    #TODO - Finish the code

# ["Health", "Health", "Armor", "Armor", "Health"]

#Print out the stats of the player in a readable format
def view_stats():
  print("\n------------------------\n")
  print(f"-- Player Statistics --\n")
  print(f"1.Name: {player["name"]}")
  print(f"2.Health: {player["health"]}")
  print(f"3.Max Health: {player["max_health"]}")
  print(f"4.Armour: {player["armour"]}")
  print(f"5.Gold: {player["gold"]}")
  if len(player["potions"])==0:
    print(f"6.Potions : --- No potions available --- ")
  else:
    print(f"6.Potions: {player["potions"]}")
  if len(player["weapons"])==0:
    print(f"6.Weapons : --- No weapons available --- ")
  else:
    print(f"6.Weapons: {player["weapons"]}")
  print("\n--------------------------\n")


def shop():
  pass
  
def boss_fight():
  pass








#-----------------
#  Main Game Loop
#-----------------
# Ask the user to enter their name
# The user to continuously input a number to select an option
# If the number matches the option, start the relevant procedure
# If the number is the quit option, end the game


def main():
  name = input("Enter your name: ")
  # Assign the name to the dictionary of player
  player["name"]=name
  while True:
    print("""=====Main Menu=====
          
1 - Fight Enemy
2 - View Stats
3 - Go to Shop
4 - Fight the Boss
5 - Quit
           """)
    choice= input("> ")
    if choice == "1":
      fight_enemy()
    elif choice == "2":
      view_stats()
    elif choice =="3":
      shop()
    elif choice == "4":
      boss_fight()
    elif choice == "5":
      break
    else:
      print("Invalid input!")

main()



