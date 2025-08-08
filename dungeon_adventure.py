import random  
name = input("Enter your name traveler:")
health = 10
inventory = []
print (f"Welcome to the Dungeon {name}. Your current health is {health} and your current inventory is {inventory} ")
treasure = {"Gold Gloves":40, "Helmet":50, "Sword":20, "Ring of Fortune":75, "Mask of Misery":100}
def end_game():
    total_value = 0
    for item in inventory:
        if item in treasure:
            total_value += treasure[item]
    print("Game Summary")
    print(f"Final Health: {health}")
    print(f"Inventory: {inventory}")
    print(f"Total Treasure Value: {total_value} gold")
    print("Thanks for playing!")
    exit()
for room in range(1,6):
    while True:
        action = input(f"""You have entered room {room}\n 
    Type the number of what you would like to do: 
    1. Search for treasure
    2. Move to next room
    3. Check health and inventory
    4. Quit the game
          """)
        if action == "1":
            roll = random.choice(["treasure", "trap"])
            if roll == "treasure":
                inventory.append(random.choice(list(treasure)))
                print(f"Yoo found{inventory} Huzzah!")
            else:
                health -= 2 
                print(f"Fell in a trap, you have lost two health. Your current health is {health}")
                if health <= 0:
                    print(f"You have died in the dungeon")
                    end_game()
        elif action == "2":
            print(f"You have moved Rooms")
            break
        elif action == "3":
            print(f"Player health: {health}")
            print(f"Players inventory: {inventory}") 
        elif action == "4":
            print(f"you have quit game")
            end_game()
        else:
            print(f"Invalid action, try again")
end_game()