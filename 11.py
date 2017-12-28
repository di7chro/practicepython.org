# practicepython.org
# Övning 11
#
# Ask the user for a number and determine whether the number is prime or not. 
# Take this opportunity to practice using functions.

def isPrime(number):
    if number == 1:     # Talet 1 är ett specialfall
        prime = False
    elif number == 2:   # ...och det är även 2
        prime = True
    else:
        prime = True    # Anta att talet är ett primtal
        for i in range(2, int ((number / 2))+1):    # Skapa lista med alla siffror upp till talet 
            if number % i == 0:                     # Kolla resten efter divisionen. 0 -> Inget primtal
                prime = False
                break        
    return prime

def main():
    try:
        number = int (input ("Ange ett tal: "))
    except ValueError:
        print("Det där var inget tal. Bara tal kan såklart vara Primtal")
    else:
        if isPrime(number):
            print("Talet {} är ett Primtal.".format(number))
        else:
            print("Nope! Talet {} är ett vanligt jädra tal". format(number))
if __name__ == "__main__": main()