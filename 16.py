# practicepython.org
# Övning 16
# 
# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
# numbers, and symbols. The passwords should be random, generating a new password every 
# time the user asks for a new password. Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or 
# two from a list.

import random
def passGen1():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#¤%&/()=+-.,*/"
    numChars = 10
    password = "".join(random.sample(chars, numChars))
    print("Random Password: " + password)

def passGen2():
    # Skapa en sträng med olika tecken att ta med
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!#¤%&/()=+-.,*/"
    
    # Fråga vilka teckenrymder som skall kunnas väljas från
    inc_lower = input("Skall jag ta med lower [y/n]: ")
    inc_upper = input("Skall jag ta med upper [y/n]: ")
    inc_numbers = input("Skall jag ta med numbers [y/n]: ")
    inc_special = input("Skall jag ta med special [y/n]: ")
        
    # Gör sträng av valda tecken
    chars = ""
    if inc_lower == 'y':
        chars = chars + lower
    if inc_upper == 'y':
        chars = chars + upper
    if inc_numbers == 'y':
        chars = chars + numbers
    if inc_special == 'y':
        chars = chars + special
    
    # Avsluta om man inte valt några tecken
    if len(chars) == 0:
        print("Du har inga tecken att välja på, avslutar...")
        quit()

    # Hämta in lösenordslängden med try/except.
    # Om man inte anger en siffra i intervallet kastas ett Exception 
    try:
        numChars = int(input("Hur långt skall det vara[0-{}]: ".format(len(chars))))
        if numChars not in range(0, len(chars)):
            raise ValueError
    except ValueError:
        print("Du lyckades inte skriva in siffran, avslutar...")
        quit()
    password = "".join(random.sample(chars, numChars))
    print("Generated Password: " + password)
    
def main():
    passGen1()
    passGen2()
    
if __name__ == "__main__": main()