# The Collatz Conjecture

# Defines variables
incorrectInput = "Incorrect input. You must enter a number greater than 1."

# Main program loop
while True:
    # Attempts to change the user's input from a string to a integer
    try:
        number = int(input("Choose a number greater than 1. "))
    except ValueError:
        print(incorrectInput)
        continue

    isInteger = isinstance(number, int)  # Checks if the number is an integer
    if (
        isInteger == True and number > 1
    ):  # Performs the code below if the number is an integer and the number is greater than 1
        moves = 0
        while number != 1:
            if (number % 2) == 0:
                number = number / 2
                moves = moves + 1
                print(number)
            else:
                number = (number * 3) + 1
                moves = moves + 1
                print(number)

        print(f"It took {moves} moves to get to 1.\n")

    else:
        print(incorrectInput)
        continue