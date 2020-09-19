'''This version now debits points if you choose to start the game over, rather than resetting everything. It is also quite snarky.'''

import random

fruits = ['apple', 'banana', 'cherry', 'orange', 'lemon', 'strawberry']
turns = 0
monies = 0
playing_game = True

print("Welcome to Jackpot! Spin the wheel and see how many points you can get!")

while playing_game:
    roll = input("Roll Tide? Y or N: ")

    if roll[0].lower() == 'y':
        turns += 1

        roll_one = random.choice(fruits)
        roll_two = random.choice(fruits)
        roll_three = random.choice(fruits)

        print(roll_one, roll_two, roll_three)

        if roll_one == roll_two and roll_two == roll_three:
            monies += 5000
            print('Jackpot! Looking sharp! You have {} points.'.format(monies))
        elif roll_one == roll_two or roll_one == roll_three:
            monies += 2000
            print('Two out of three, not too shabby! You have {} points.'.format(monies))
        elif roll_two == roll_three:
            monies += 2000
            print('Two out of three, solid! You have {} points.'.format(monies))
        else:
            print('No matches. No points for you! Current point balance: ', monies)

        if turns == 3:
            print("You are out of turns.")
            play_again = input('Would you like to keep going? Y or N? ')
            if play_again.lower() == 'y':
                monies -= 1500
                if monies < 0:
                    print("Hmmm, you have less than 1500 points. That's not enough to cover a new game. Sorry, not sorry. ;)")
                    print("Better luck next time.")
                    break
                else:
                    confirm = input("Okay, new game. It's gonna cost you though, you sure? Y or N ")
                    if confirm.lower() == 'y':
                        print("You're the boss. 1500 points have been debited from your score. Good luck!")
                        print('Current Score: ', monies)
                        turns = 0
                        continue
                    elif confirm.lower() == 'n':
                        print('Wise move, see ya later!')
                        print('Final Score: ', monies)
                        break
                    else:
                        print("That was an invalid response, my friend. Let's try that again.")
                        continue
            elif play_again.lower() == 'n':
                print("Final score: {}".format(monies))

                if monies >= 5000:
                    print("You're a superstar!")
                elif 2500 <= monies < 5000:
                    print("Not bad!")
                elif monies > 2500:
                    print("The odd are not in your favor...")

                print("Come back soon!")
                break

    elif roll[0].lower() == 'n':
        print('Then why are you here? Deuces!')
        break
    else:
        print('Response does not compute, please try again.')
        continue
