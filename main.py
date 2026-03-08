import os
import time
import random
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

class data:
  def __init__(self, player, health, damage, defense, armour, crit):
    self.player = player
    self.health = health
    self.damage = damage
    self.defense = defense
    self.armour = armour
    self.crit = crit

  def accept(self, player, health, damage, defense, armour, crit):
    insert = data(player, health, damage, defense, armour, crit)
    list.append(insert)
    
  def display(self, insert):
    print("\nName : ", insert.player)
    print("Health : ", insert.health)
    print("Attack Damage : ", insert.damage)
    print("Defense : ", insert.defense)
    print("Armour : ", insert.armour)
    print("Critical Chance : ", insert.crit,"%\n")

  def search(self, key):
    for i in range(len(list)):
      if (list[i].player.lower() == key.lower()):
        return i
      return None

  def delete(self, key):
    i = insert.search(key)
    if i != None:
      del list[i]
      input("Player deleted.")
    else:
      input("Player not found.")

list = []
insert = data("", 0, 0, 0, 0, 0)


def home():
  while True:
    clear()
    print("Welcome to the game!")
    print("1. Add New Player")
    print("2. Remove Player")
    print("3. Check All Players")
    print("4. Start Game")
    print("5. Exit")
    temp_a = input("What would you like to do? (1-3): ")
    if temp_a == "1":
      new_player()
      
    elif temp_a == "2":
      clear()
      key = input("Enter the name of the player you want to remove: ")
      insert.delete(key)
        
    elif temp_a == "3":
      if len(list) == 0:
        clear()
        input("No players have been created.")
      else:
        clear()
        print("Player List: ")
        for i in range(len(list)):
          insert.display(list[i])
        input("\n")
        
    elif temp_a == "4":
      clear()
      if len(list) > 0:
        print("Game is starting...")
        time.sleep(4)
        game()
      else:
        print("No players have been created.")
      
    elif temp_a == "5":
      print("Thank you 4 playing!")
      time.sleep(5)
      exit()
    
def new_player():
  clear()
  global list
  
  # NAME SELECTION
  while True:
    clear()
    player = input("Enter your name: ")
    check_1 = any(c.isalpha() for c in player)
    check_2 = any(c.isdigit() for c in player)
    if check_1 or check_2:
      temp_a = input("\nYou have selected the name "+player+". Are you sure you want to use this name? (y/n): ")
      if temp_a == "y":
        clear()
        input("You have selected the name "+player+".")
        clear()
        break
    else:
      input("\nInvalid name. Please enter a name with at least one letter or number.")
      clear()
      
  # SP DISTRIBUTION    
  health = 100
  damage = 20
  defense = 10
  armour = 0
  crit = 0
  sp = 20
  while True:
    while sp > 0:
      clear()
      print("You have "+str(sp)+" skill points left to spend.")
      print("1. Health: "+str(health))
      print("2. Attack Damage: "+str(damage))
      print("3. Defense: "+str(defense))
      print("4. Armour: "+str(armour))
      print("5. Crit: "+str(crit)+"%")
      temp_b = input("What would you like to spend your skill points on? (1-5): ")
      if temp_b == "1":
        health += 5
        sp -= 1
      elif temp_b == "2":
        damage += 5
        sp -= 1
      elif temp_b == "3":
        defense += 5
        sp -= 1
      elif temp_b == "4":
        armour += 5
        sp -= 1
      elif temp_b == "5":
        crit += 5
        sp -= 1
      else:
        input("\nInvalid input. Please enter a number between 1 and 5.")
        clear()
        
    clear()
    print("1. Health: "+str(health))
    print("2. Attack Damage: "+str(damage))
    print("3. Defense: "+str(defense))
    print("4. Armour: "+str(armour))
    print("5. Critical Chance: "+str(crit))
    temp_a = input("\nYou have spent all your skill points.\n\nAre you sure you want to keep these stats? (y/n):")
    if temp_a.lower() == "y":
      clear()
      input("You have selected the following stats:\nHealth: "+str(health)+"\nAttack Damage: "+str(damage)+"\nDefense: "+str(defense)+"\nArmour: "+str(armour)+"\nCritical Chance: "+str(crit))
      clear()
      break
    elif temp_a.lower() == "n":
      health = 100
      damage = 20
      defense = 10
      armour = 0
      crit = 0
      sp = 20
  insert.accept(player, health, damage, defense, armour, crit)
  
difficulty = 1

def game():
  while True:
    global difficulty
    clear()
    total_player = len(list)
    enemy_health = (random.randint(1,90) + difficulty) * total_player
    enemy_damage = (random.randint(1,20) + difficulty) * total_player
    enemy_defense = (random.randint(1,10) + difficulty) * total_player
    enemy_armour = (random.randint(0,10) + difficulty) * total_player
    enemy_crit = (random.randint(0,10) + difficulty) * total_player
    
    print("Enemy Stats: ")
    print("Health: "+str(enemy_health))
    print("Attack Damage: "+str(enemy_damage))
    print("Defense: "+str(enemy_defense))
    print("Armour: "+str(enemy_armour))
    print("Critical Chance: "+str(enemy_crit)+"%\n")
    input()
    clear()
    print("The battle has begun!")
    current_player_index = 0
    players_alive = True
    while enemy_health > 0 and players_alive:
      current_player = list[current_player_index]
      if current_player.health > 0:
        print("Player "+str(current_player_index+1))
        insert.display(current_player)
        input()
        clear()
        print("Player "+str(current_player_index+1)+" is attacking!")
        time.sleep(2)
        
        # CRIT
        rng = random.randint(1,100)
        if rng <= (current_player.crit):
          crit_multiplier = random.uniform(1.8,3.0)
          print("Critical Hit!")
        else:
          crit_multiplier = 1
          
        # DAMAGE
        prev_health = enemy_health
        total_damage = (current_player.damage) * crit_multiplier
        total_defense = 1 - (enemy_defense / 100)
        damage_dealt = total_damage * total_defense
        enemy_health -= damage_dealt
        blocked = prev_health + (prev_health - enemy_health)
        if enemy_health < 0:
          enemy_health = 0
        
        # EX
        input(str(current_player.damage) + " * " + str(crit_multiplier) + " = " + str(total_damage) + " DAMAGE!")
        input(str(blocked) + " DAMAGE BLOCKED!")
        time.sleep(2)
        input(str(damage_dealt) + " DAMAGE DEALT!")
        if enemy_health <= 0:
            print("Enemy has been defeated by Player " + str(current_player_index + 1) + "!")
            break
      else:
        print("Player "+str(current_player_index+1)+" is already defeated.")
      
      current_player_index = (current_player_index + 1) % len(list)
      
      if current_player_index == 0: # All players have attacked (or are defeated)
        if enemy_health > 0:
          print("\nEnemy is attacking!\n")
          time.sleep(2)
          
          for i in range(len(list)):
            if list[i].health > 0:
              print("Enemy attacking Player " + str(i+1) + "!")
              
              # Enemy Crit
              enemy_rng = random.randint(1,100)
              if enemy_rng <= enemy_crit:
                enemy_crit_multiplier = random.uniform(1.5,2.5)
                print("Critical Hit!")
              else:
                enemy_crit_multiplier = 1
              
              # Enemy Damage Calculation
              player_prev_health = list[i].health
              enemy_total_damage = enemy_damage * enemy_crit_multiplier
              player_total_defense = 1 - (list[i].defense / 100)
              enemy_damage_dealt = enemy_total_damage * player_total_defense
              list[i].health -= enemy_damage_dealt
              enemy_blocked = player_prev_health - (player_prev_health + list[i].health)
              if list[i].health < 0:
                list[i].health = 0
              
              input(str(enemy_damage) + " * " + str(enemy_crit_multiplier) + " = " + str(enemy_total_damage) + " DAMAGE!")
              input(str(enemy_blocked) + " DAMAGE BLOCKED!")
              time.sleep(2)
              input(str(enemy_damage_dealt) + " DAMAGE DEALT!")
              
              if list[i].health <= 0:
                print("Player " + str(i+1) + " has been defeated!")
                
              input()
              clear()
        else:
          break # Enemy is defeated, no need to attack
          
      # Check if any players are still alive
      players_alive = any(player.health > 0 for player in list)
      if not players_alive:
        print("All players have been defeated!")
        break
        
    clear()
    if enemy_health <= 0:
      input("The enemy has been defeated. Nice work!")
      difficulty += random.randint(1,3)
      print("Difficulty increased to "+str(difficulty)+".")
      
    else:
      input("You have been defeated!")
      break
  
home()