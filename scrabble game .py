## File : CS112_A1_T2_ Game 2 _20230337
## Purpose: 1 ) Players take turns choosing numbers from the list.
##          2 ) If a player successfully picks three numbers that sum up to 15,
##              that player wins the game.
##          3 ) If all the numbers are used up and no player has achieved the goal of getting exactly 15
##              with three numbers, the game ends in a draw.
## Author: Mohamed Refaat Mohamed Awad
## ID : 20230337

def number_scrabble():

    print("Welcome to number scrabble game")

    # List of available numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Lists to store chosen numbers by each player
    list_1 = []
    list_2 = []

    while True:
        # Display available numbers
        print(numbers)

        # Player 1's turn
        while True:
            try:
                # Player 1 chooses a number
                player_1 = int(input("Player 1: choose a number = "))
                if player_1 not in numbers:
                    # check if the number isn't a valid
                    print("Please enter a valid number")
                    continue
            except ValueError:
                # If the input cannot be converted to an integer, prompt to enter a valid number
                print("Please enter a valid number")
                continue
            break

        # Remove and update the available numbers and add it to Player 1's list
        numbers.remove(player_1)
        list_1.append(player_1)

        print ("============================")
        # Check if Player 1 has won
        if test(list_1):
            print("Player 1 is the winner!! your list is : ", list_1)
            break

        # Check for a draw
        if numbers == []:
            print("Draw!!")
            break

        # Display available numbers after Player 1's turn
        print(numbers)

        # Player 2's turn
        while True:
            try:
                # Player 2 chooses a number
                player_2 = int(input("Player 2: choose a number = "))
                if player_2 not in numbers:
                     # check if the number isn't a valid
                    print("Please enter a valid number")
                    continue
            except ValueError:
                # If the input cannot be converted to an integer, prompt to enter a valid number
                print("Please enter a valid number")
                continue
            break

        # Remove and update the available numbers and add it to Player 2's list
        numbers.remove(player_2)
        list_2.append(player_2)
        print ("============================")
        
        # Check if Player 2 has won
        if test(list_2):
            print("Player 2 is the winner!! your list is : ", list_2)
            break
        
def test(numbers):
    # Check if there are at least 3 numbers in the list
    if len(numbers) < 3:
        return False
    
    # Nested loops to iterate over all possible combinations of three numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                # Check if the sum of the current triplet is equal to 15
                if numbers[i] + numbers[j] + numbers[k] == 15:
                    return True
    return False

number_scrabble()