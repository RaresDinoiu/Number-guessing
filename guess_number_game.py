import random

number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))

while guess != number:
    if guess < number:
        print ("Wrong! you need to gues higher. Try again.")
        guess = int(input("\nGuess a number between 1 and 50: "))
    else:
        print ("Wrong! you need to guess lower. Try again")
        guess = int(input("\nGuess a number between 1 and 50: "))

print ("You guessed the number correctly!")


