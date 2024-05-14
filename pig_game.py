# allow the user to roll a dice
# ask user if they want to continue, if stopped, add the score to total

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Enter a number between 2 and 4.")
            continue
    else:
        print("Invalid! Try again")
        
max_score = 50 # set as required
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index+1} turn has started")
        print(f"Your total score is {player_scores[player_index]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            
            else:
                current_score += value
                print(f"You rolled a: {value}")
            print("Your score is: ", current_score)
        
        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])
        
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print(f"Player number {winning_index} is winner with score of {max_score}")