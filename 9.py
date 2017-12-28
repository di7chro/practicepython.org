# practicepython.org
# Övning 9
#
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, 
# too high, or exactly right. 
from random import randint

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

def main():
    secret = randint(1, 9)
    guess = 0
    while True:
        guess = input("Gissa på talet: ")
        
        if guess == "quit":
            print("Avslutar")
            break
        elif guess.isdigit() == False:
            print("Öh, det var inget tal!")
            continue
        elif int(guess) < secret:
            print("Du gissade för lågt")
        elif int(guess) > secret:
            print("Du gissade för högt")
        elif int(guess) == secret:
            print("Du gissade rätt!")
            break
        else:
            print("Det där var nog inget tal!")
if __name__ == "__main__": main()