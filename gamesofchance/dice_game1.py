import random

final_score = 0
winning_score = 10
game_play = True

print("Let's play a game!")

while game_play:
    print("Let's roll some die and see if you get higher than 10!")

    player_roll = input("Roll die? Y or N: ")

    if player_roll.lower() == 'y':
        roll_one = random.randint(1, 6)
        roll_two = random.randint(1, 6)
        roll_three = random.randint(1, 6)

        final_score = roll_one + roll_two + roll_three

        if final_score >= winning_score:
            print("You win!")
            print("Winning score: ", final_score)
        else:
            print("No soup for you!")
            print("Your score: ", final_score)
            break
    elif player_roll.lower() == 'n':
        print("Maybe next time!")
        break
    else:
        print("You've entered an invalid response. Try again.")
        continue
