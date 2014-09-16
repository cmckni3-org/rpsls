#!/usr/bin/env python

import random
# Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
NAME_MAPPING = [(0, "rock"), (1, "Spock"), (2, "paper"), (3, "lizard"), (4, "scissors")]

def number_to_name(number):
    for (key, value) in NAME_MAPPING:
        if key == number:
            return value

def name_to_number(name):
    for (key, value) in NAME_MAPPING:
        if value == name:
            return key

def player_wins(player_choice):
    # convert name to player_number using name_to_number
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number   = random.randrange(0, 5)
    # compute difference of player_number and comp_number modulo five
    difference    = (player_number - comp_number) % 5
    # convert comp_number to name using number_to_name
    comp_name     = number_to_name(comp_number)
    # print results
    print("Player chooses", player_choice)
    print("Computer chooses", comp_name)
    # use if/elif/else to determine winner
    if difference == 0:
        print("Player and computer tie!")
        return None
    elif difference > 2:
        print("Computer wins!")
        return False
    else:
        print("Player wins!")
        return True

def print_game_title():
    print('{:-^80}'.format(''))
    print('{:^80}'.format("Rock Paper Scissors Lizard Spock"))

def print_final_score(computer, human):
    print('{:-^80}'.format(''))
    print('{:^80}'.format('Final Score'))
    print('{:^40} {:^40}'.format('Computer', 'Human'))
    print('{:^40} {:^40}'.format(computer, human))
    print('{:-^80}'.format(''))

def main():
    computer = 0
    human    = 0
    play     = True
    print_game_title()
    while play:
        print('{:-^80}'.format(''))
        player_choice = input("Please, enter a choice <rock, Spock, paper, lizard, scissors>: ")
        if name_to_number(player_choice) != None:
            winner = player_wins(player_choice)
            if winner:
                human += 1
            elif winner == False:
                computer += 1
        else:
            print("Invalid choice")
        play_again = input("Play again? <Y, n>: ")
        play = (play_again == 'Y' or play_again == 'y')
    print_final_score(computer, human)

if __name__ == "__main__":
    main()
