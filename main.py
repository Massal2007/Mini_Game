# Import random
import random
from time import sleep

# Score on game
lives_remaining = 4

# Pick the random number
rand_num = random.randint(1, 50)
# print(rand_num)

print('The number can be from 0-50\nGood Luck')

while True:

    # The player guesses the AI's number
    guess = int(input('Try yo guss the AIs number\n'))

    # The guess is equal at what AI picked
    if guess == rand_num:
        print('You won! You guessed right the AIs number\n')
        print('Your life is on: ', lives_remaining)
        sleep(5)
        break

    # Guess - Random Number
    all_together = guess - rand_num
    all_together1 = rand_num - guess

    # The guess is bigger than the AI's number
    if 3 >= all_together > 0:
        print('Your number is a little bit bigger than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)
    elif 3 < all_together < 15:
        print('Your number is bigger than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)
    if all_together >= 15:
        print('Your number is much bigger than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)

    # The guess is smaller than the AI's number
    if 0 < all_together1 <= 3:
        print('Your number is a little bit smaller than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)
    elif 3 < all_together1 < 15:
        print('Your number is smaller than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)
    if all_together1 >= 15:
        print('Your number is much smaller than the chosen one\n')
        lives_remaining = lives_remaining - 1
        print('Your life is on: ', lives_remaining)
        if lives_remaining == 0:
            print('You Lost! :{ ')
            sleep(5)

    if lives_remaining == 0:
        resume = str(input('Do you want to to start a new one? Type [y] to play or [n] to close the game\n'))
        if resume == 'n':
            break
        else:
            continue
