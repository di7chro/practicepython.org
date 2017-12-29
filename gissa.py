# Gissningsspel av Emma Ohlsson
# 29 December 2017
#

from random import randint

namn = input("Välkommen! Vad heter du? ")
print("Hej {}! Nu ska du gissa på ett tal melölan 0 och 10.".format(namn))

hemligt = randint(0,10)
antal = 0

while True:
    gissning = int (input("Vad gissar du på? "))
    antal = antal + 1
    if gissning == hemligt:
        print("Grattis! ")
        break
    elif gissning < hemligt:
        print("För lågt")
    
    elif gissning > hemligt:
        print("För högt")
    
print("Bra jobbat", namn)
print("Du gissade rätt efter {} försök.".format(antal))