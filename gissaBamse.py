# Gissningsspel av Emma Ohlsson
# Gissa karaktärer från Bamse
# 19 Februari 2018
#

from random import randint
Lista=["bamse","skalman","farmor","brummelisa","lilleskutt","vargen","brumme"]
namn=input("Välkomm en! Vad heter du? ")
print("Hej {}! Gissa på någon i Bamse.".format (namn))
hemlig=randint(0,len(Lista))
antal = 0

while True:
    antal = antal + 1
    Gissning=input("Vem gissar du på? ")
    if Gissning==Lista[hemlig]:
        break

print("Bra jobbat {}! Du gissade rätt efter {} försök!".format (namn, antal))