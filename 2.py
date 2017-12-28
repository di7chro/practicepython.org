# practicepython.org
# Övning 2
#
# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate 
# message to the user. 
# Extras:
# If the number is a multiple of 4, print out a different message

def main():
    siffra = input("Ange en siffra: ")
    siffra = int(siffra)
    if siffra % 4 == 0:
        print("Du skrev in {} vilket är JÄMNT tal som är delbart med 4.".format(siffra))        
    elif siffra % 2 == 0:
        print("Du skrev in {} vilket är JÄMNT tal".format(siffra))
    else:
        print("Siffran {} är ett UDDA tal".format(siffra)) 
if __name__ == "__main__": main()

