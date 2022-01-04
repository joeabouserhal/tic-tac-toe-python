from rich import print
from rich.console import Console
import os
import platform

"""
Tic Tac Toe
-----------
Welcome to this basic simple tic tac toe game that i wrote in literally like 2 hours and i had
a lot of fun with it.
Don't expect any sort of updates to it because i couldn't bother less
But thanks for checking it ot anyways!!!
"""

# git test 1
# git test 2

console = Console()
empty = " "
board_pos = [empty] * 9


def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("reset")


def main():
    select_character()


def select_character():
    console.print(r"""
[white]
 $$\ $$\   $$\   $$\  $$$$$$\
  $$ \$$ \  $$ |  $$ |$$  __$$\
$$$$$$$$$$\ \$$\ $$  |$$ /  $$ |
\_$$  $$   | \$$$$  / $$ |  $$ |
$$$$$$$$$$\  $$  $$<  $$ |  $$ |
\_$$  $$  _|$$  /\$$\ $$ |  $$ |
  $$ |$$ |  $$ /  $$ | $$$$$$  |
  \__|\__|  \__|  \__| \______/
[/white]
""", justify="center")
    console.print("Welcome to Tic Tac Toe!", justify="center", end="\n\n\n\n\n")
    player = console.input("Please pick [green]X[/green] or [green]O[/green]: ").upper()
    if player != 'X' and player != 'O':
        clear()
        print("Wrong input, please try again!")
        select_character()
    clear()
    play(player)


# function that prompts user to pick position, then check the board
def play(player: chr):
    board = f" {board_pos[0]} | {board_pos[1]} | {board_pos[2]}\n" \
            f"-----------\n" \
            f" {board_pos[3]} | {board_pos[4]} | {board_pos[5]}\n" \
            f"-----------\n" \
            f" {board_pos[6]} | {board_pos[7]} | {board_pos[8]}\n"
    print(board)
    picked_position = console.input(f"player {player} please enter the number you would like to cross out: ")
    try:
        picked_position = int(picked_position)
    except (Exception, ValueError):
        clear()
        print("Wrong input!")
        play(player)

    if board_pos[picked_position - 1] == empty and 1 <= picked_position <= 9:
        board_pos[picked_position - 1] = player
        check_for_win(player)
        if player == 'X':
            clear()
            play('O')
        else:
            clear()
            play('X')
    else:
        if board_pos[int(picked_position) - 1] == empty:
            clear()
            print("Place is already taken try again!")
            play(player)
        else:
            clear()
            print("Wrong input try again!")
            play(player)


# function that checks whether the player has won
def check_for_win(player: chr):
    if board_pos[0:3] == [player] * 3:
        win(player)
    elif board_pos[3:6] == [player] * 3:
        win(player)
    elif board_pos[6:9] == [player] * 3:
        win(player)
    elif [board_pos[0], board_pos[3], board_pos[6]] == [player] * 3:
        win(player)
    elif [board_pos[1], board_pos[4], board_pos[7]] == [player] * 3:
        win(player)
    elif [board_pos[2], board_pos[5], board_pos[8]] == [player] * 3:
        win(player)
    elif [board_pos[0], board_pos[4], board_pos[8]] == [player] * 3:
        win(player)
    elif [board_pos[2], board_pos[4], board_pos[6]] == [player] * 3:
        win(player)
    elif empty not in board_pos:
        tie()


# display the tie screen
def tie():
    clear()
    print("[black on yellow]Uh oh it was a tie[black on yellow]")
    selection = console.input("Enter 0 to quit or 1 to play again: ")
    if selection == '0':
        quit()
    elif selection == '1':
        clear()
        clear_board()
        select_character()
    else:
        clear()
        tie()


# display the winning screen
def win(winner: chr):
    clear()
    print(f"[black on green]Player {winner} has won!!![/black on green]")
    selection = console.input("Enter 0 to quit or 1 to play again: ")
    if selection == '0':
        quit()
    elif selection == '1':
        clear()
        clear_board()
        select_character()
    else:
        clear()
        win(winner)


# clear the board to restart the game
def clear_board():
    global board_pos
    board_pos = [empty] * 9


if __name__ == "__main__":
    main()
