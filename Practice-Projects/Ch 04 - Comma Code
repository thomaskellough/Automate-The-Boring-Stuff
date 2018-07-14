#! python3
# comma_code.py - Will have the user input items in a list then return the
# list with commas as well as 'and' before the last item


# Function that edits the list. You pass one argument inside, 'my_list'.
# The for loop will allow the function to run for the range of any list.
# You need to do len(my_list) - 1 since you first only want to print all items EXCEPT for the last.
# The second argument in the first print statement is end='' since it's normally defaulted
# to a new line. This makes it so you will print your entire list on one line.
# The second print statement is the for printing last item and adding the word 'and'. Since your for loop
# is oly for the range of the length of the list MINUS 1, you still need one more item to print out
# You put the last print statement outside the for loops so it will print once it's finished.
# Make sure you do my_list[i + 1] or you will repeat your second to last item
def my_function(my_list):
    for i in range(len(my_list) - 1):
        print(my_list[i] + ', ', end='')
    print('and ' + my_list[i + 1])


# You need to first initialize an empty list. Do this before your while loop.
spam = []
# A while True block while run continuously until a break statement is performed.
# The user needs an option to break out of the loop. This is done by pressing enter without
# typing anything else. Otherwise, anything you type, (string, integer, character, etc) will be
# appended to the empty list with .append(item)
while True:
    item = input('Please enter an item for your list or press enter to stop.\n')
    if item is not '':
        spam.append(item)
    else:
        break

# Once the function is created, just pass the list name inside after calling the function
my_function(spam)
