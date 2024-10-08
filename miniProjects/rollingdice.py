#  this is a simple program that allow a max of four and a min of two to play a rolling dice game
#
#  step 1 : allow the user to role the dice
import random

def roll():
    min_value = 1
    max_value = 6

    role = random.randint(min_value, max_value)
    return role

while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 and 4 players!')
    else:
        print('Invalid Input, try again')

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print(f'\nPlayer number {player_idx + 1} turn has just started!')
        print(f'your total score is: {player_score[player_idx]} \n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)/(n)? ')
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You Rolled a: {value}')

            print(f'Your current score is: {current_score}')
        player_score[player_idx] += current_score
        print(f'Your total score is: {player_score[player_idx]}')

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f'Players number {winning_idx + 1} is the winner with a score of: {max_score}')