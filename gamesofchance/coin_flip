import random

play_game = True
coin_options = ['H', 'T']
points = 0

while play_game:
    print("Let's play a game.")
    print("You'll flip a coin, if you get heads you earn one point. Tails, you lose one point.")
    print("Try to get to five points to win!")
    flip_coin = input("Flip the coin? Y or N? ")
    if flip_coin.lower() == 'y':

        coin_result = random.choice(coin_options)
        if coin_result == 'H':
            points += 1
        else:
            points -= 1

        if points == 5:
            print("You have five points! Bravo! You won!")
            break
        elif points == 1:
            print("The result was {}. You now have {} point. Keep it up!".format(coin_result, points))
            continue
        elif points == -3:
            print("You have negative three points!")
            play_again = input("Yikes, do you want to try again? Y or N?")
            if play_again.lower() == 'y':
                points = 0
                turns = 0
                continue
            elif play_again.lower() == 'n':
                print("Better luck next time.")
                break
            else:
                print("Sorry, that's an invalid response.")
                break
        else:
            print("The result was {}. You now have {} points.".format(coin_result, points))
            continue
    elif flip_coin.lower() == 'n':
        print("Okay, see you later!")
        break
    else:
        print("You have entered an invalid response. Please try again")
        continue
