"""
Assignment: Tic Tac Toe
Author: Alec Byington
Date: 9/17/22
"""

def main():
    # Set up
    position = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    play = True

    while play:
        ready = input(f"Are you ready to begin? (Y/N): ")
        if ready.lower() == "y":
            player = input(f"Begin as (X) or (O)?")
            if player.lower() == "x":
                x_first(position)
            else:
                o_first(position)

        elif ready.lower() == "n":
            print("Thanks for Playing!")
            play = False
        
        else:
            print("Error")

def draw_board(position):
    board = (f"{position[1]} | {position[2]} | {position[3]}\n- + - + -\n{position[4]} | {position[5]} | {position[6]}\n- + - + -\n{position[7]} | {position[8]} | {position[9]}\n")
    print (board)

def x_first(position):
    # Game has begun!
    print()
    draw_board(position) # Turn 1
    choice = int(input(f"X's turn to choose a square (1-9): "))
    position[int(choice)] = "X"
    print()
    
    draw_board(position) # Turn 2
    choice = int(input(f"O's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 3
    choice = int(input(f"X's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 4
    choice = int(input(f"O's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 5
    choice = int(input(f"X's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 6 - Early Game
    choice = int(input(f"O's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 7 - Mid Game
    choice = int(input(f"X's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 8 - Mid Game
    choice = int(input(f"O's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 9 - Late Game or Draw
    choice = int(input(f"X's turn to choose a square (1-9): "))
    if not position[choice] in {"X", "O"}:
        position[int(choice)] = "X"
    print()

    print("Good Job! Thanks for Playing!")
    print()

def o_first(position):
    # Game has begun!
    print()
    draw_board(position) # Turn 1
    choice = int(input(f"O's turn to choose a square (1-9): "))
    position[int(choice)] = "O"
    print()
    
    draw_board(position) # Turn 2
    choice = int(input(f"X's turn to choose a square (1-9): "))
    position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 3
    choice = int(input(f"O's turn to choose a square (1-9): "))
    position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 4
    choice = int(input(f"X's turn to choose a square (1-9): "))
    position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 5 - Early Game
    choice = int(input(f"O's turn to choose a square (1-9): "))
    position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 6 - Early Game
    choice = int(input(f"X's turn to choose a square (1-9): "))
    position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 7 - Mid Game
    choice = int(input(f"O's turn to choose a square (1-9): "))
    position[int(choice)] = "O"
    print()

    draw_board(position) # Turn 8 - Mid Game
    choice = int(input(f"X's turn to choose a square (1-9): "))
    position[int(choice)] = "X"
    print()

    draw_board(position) # Turn 9 - Late Game or Draw
    choice = int(input(f"O's turn to choose a square (1-9): "))
    position[int(choice)] = "O"
    print()

    print("Good Job! Thanks for Playing!")
    print()

def o_choice(position): # Working on #
    while True:
        try:
            choice = int(input(f"O's turn to choose a square (1-9): "))
        except ValueError:
            print("Invalid Input")
        else:
            if not position[choice] in {"X", "O"}:
                position[int(choice)] = "O"
                continue
            else: 
                break

# --- End of Program --- #   

if __name__ == "__main__":
    main()