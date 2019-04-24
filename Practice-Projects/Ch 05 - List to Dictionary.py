#! python3
# fantasy_game_inventory.py - adds loot obtained from a dragon into a players
# inventory and prints it out on the screen


# See fantasy_game_inventory.py for explanation of this function
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total Items: ' + str(item_total))


# This function can be a bit tricky. You need to pass two arguments inside of it.
# The first argument is for the players current inventory, which should be a dictionary.
# The second argument is the items you are adding to the dictionary from the dragon loot.
# Your for loop searches for any loot inside of dragon_loot. If that particular item does NOT
# exist, you add it by setting it with a value of one using inv[loot] = 1. The key to that item
# will be what the loot is and it starts off at one. If an item does does exist, we just add one
# to the value currently inside the players inventory.
def add_to_inventory(inventory, added_items):
    for loot in dragon_loot:
        if loot not in inv:
            inv[loot] = 1
        else:
            inv[loot] += 1


# Setting up a dictionary for a player and a list for loot
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald', 'emerald', 'sapphire']
# Calling both functions. The new one created then the one from fantasy_game_inventory.py
# so you can print out the results
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
