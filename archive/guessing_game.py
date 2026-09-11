import rand
number, trials = random.randint(1, 10), 3

print('''Welcome to the Guessing Game!
You're trying to guess a number between 1 and 10.
You have only 3 trials.
Let's start!''')
print('*' * 49)

while trials > 0:
    try:
        guess = int(input('Guess the number! '))
        if guess == number:
            print(f'Hooray! You guessed the number {number} correctly!')
            break
        else:
            print('Wrong. Try again!')
        trials -= 1
    except ValueError:
        print('Invalid input. Please make sure to only guess valid numbers.')
else:
    print(f'Sorry, you failed. The number was {number}.')