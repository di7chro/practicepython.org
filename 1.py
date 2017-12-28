# practicepython.org
# Övning 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
def main():
    name = input("Vad heter du? ")
    age  = input("Ange din ålder: ")

    age = int(age)                  # Konvertera ålder till heltal
    now = datetime.datetime.now()   # Hämta in tiden just nu
    this_year = now.year            # Spara undan aktuellt år
    turn100 = this_year - age + 100 # Räkna ut årtalet man fyller 100
    
    print("Hejsan ", name)
    print("Du fyller 100 år", turn100)
if __name__ == "__main__": main()