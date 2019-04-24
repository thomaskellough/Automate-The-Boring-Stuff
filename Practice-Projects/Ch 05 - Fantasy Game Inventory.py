#! python3
# fantasy_game_inventory.py - takes a game inventory and prints it on the
# screen in a readable format


# Remember: dictionaries are created with {}
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# Dictionaires are different from lists because they have KEYS and VALUES
# For your for loop, add two variables, k for KEY and v for VALUES
# (Note: the variables can be anything, k and v are used here for simplicity)
# .items() will print both keys and values!
# Remember, you cannot add an integer to a string so you must wrap the
# value, or v, in str() to turn it into a string
# However, to obtain a total count you just add the number to item total,
# which starts at 0. (item_total += v is the same as item_total = item_total + v)
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total Items: ' + str(item_total))


display_inventory(stuff)
