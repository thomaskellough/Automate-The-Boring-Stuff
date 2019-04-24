#! python3
# table_printer.py - takes a list of lists and prints them in a justified fashion


# This specific code took me a long time to complete. There are many steps and it gets confusing
# very quickly. There are better ways to do this, such as using enumerate, but I tried to keep it
# with the content learned from this book only.


def print_table(input_list):
    # The first step is setting some variables. You want the to obtain the number of columns
    # and the number of rows. The best way to do this is calling from the list itself, this way
    # it works with any list you input. 
    # Since each inner list is the same length, you can get the number of items in each list 
    # by using len(input_list[0]). This will grab the number of items in the first list, which is
    # equal to the number of items in every other list.
    # You also need to set an empty list to hold the value of the inner string in each inner list.
    num_of_lists = len(input_list)
    items_in_lists = len(input_list[0])
    max_length_list = []

    # This part of the function obtains the longest string of each inner list. Set the initial value
    # to 0 (it will reset with each innere list) and change the value only if the new list for len(item)
    # is greater than the previous. At the end of each loop, you will append this value to your
    # list created above.
    for list in input_list:
        max_length_item = 0
        for item in list:
            if len(item) > max_length_item:
                max_length_item = len(item)
        max_length_list.append(max_length_item)
    print(max_length_list)

    # This for loop prints the results. In this specific example we want a total of four rows
    # and three columns. (Will change depending on table_data)
    # The first for loop iterates over each row, so we use items_in_list since there are 4 items
    # in each inner list.
    # The second for loop iterates over columns, so we use num_of_lists, since that is equal to
    # how many columns we want per problem given (or equal to number of itmes in each list).
    # We use rjust to get it to look like the example provided, however we need to iterate through
    # each item in the max_length_list. Since we are justifying three different columns, we use
    # the row iterator from num_of lists.
    # Last, we want to space out each word, so use end='' after each print directly, but add print('')
    # after the first for loops finishes so you can print the next line.
    for row in range(items_in_lists):
        for col in range(num_of_lists):
            print(input_list[col][row].rjust(max_length_list[col]), end=' ')
        print('')


# Data provided and calling the function
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
