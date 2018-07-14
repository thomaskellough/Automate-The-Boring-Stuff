#! python3
# collatz_sequence.py - Performs the Collatz Sequence on any number


# Introductory message
print('In order to experience the collatz sequence type in any positive number.')

# collatz function - has one if/else statement depending on if the number is even or odd
# the % is remainder. If the number entered divided by two is 0, the number is even
# You must return the result so the function can continue
# if the number is not even, it must be odd. This is why you can use else
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result


# Assign a variable to whatever number the user inputs. We put this in a try and except statement
# because if the user enters a string value the program will not crash, but will start over
# Once the user input is 1, the collatz sequence has completed. Having the function run in a while loop
# while the program is NOT 1 will cause it to run continuously until it reaches the end of the sequence
# NOTE: Put the user_input variable INSIDE the while loop. This will allow the user to put in
# a correct number. If the user_input is before the while loop your program will be stuck in
# an infinite loop
while True:
    user_input = input("Give me a number: ")
    try:
        while user_input != 1:
            user_input = collatz(int(user_input))
    except ValueError:
        print("You must enter positive integer")
# Remember to specify the type of error, in ths example ValueError refers to typing in a string
# Running the program without the try and except statement and purposely causing an error will show
# you the name of the error
# Note: there are still other errors, such as a user typing in a negative number. There are ways around
# this, but for simplicity we will not look into fixing that for our first project.
