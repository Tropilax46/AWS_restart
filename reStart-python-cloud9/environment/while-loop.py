import random
print("welcome to guess the number!")
print("the rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You Guessed {}, that is correct you win!".format(guess))
        isGuessRight = True
    else:
        print("You Guessed {}, Sorry, That isn't it. Try again.".format(guess))