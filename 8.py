# practicepython.org
# Övning 8
#
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask 
# if the players want to start a new game)

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# Jämför de två spelarna och returner vinnaren (eller Tied)
def compare(player_1, player_2):
    if player_1 == player_2:
        return "Tied"
    elif player_1 == "R" and player_2 == "S":
        return "Player 1 wins"
    elif player_1 == "R" and player_2 == "P":
        return "Player 2 wins"
    elif player_1 == "S" and player_2 == "R":
        return "Player 2 wins"
    elif player_1 == "S" and player_2 == "P":
        return "Player 1 wins"
    elif player_1 == "P" and player_2 == "R":
        return "Player 1 wins"
    elif player_1 == "P" and player_2 == "S":
        return "Player 2 wins"
    else:
        return "Invalid key pressed. Only [R P S] allowed"
    
def main():
    print("Rock Paper Scissors")
    print("Regler:")
    print("- [R]ock beats scissors")
    print("- [S]cissors beats paper")
    print("- [P]aper beats rock")

    winner = "Tied"
    while winner == "Tied":         # Loopa tills vi har en vinnare
        player_1 = input("Player 1 choose [R-P-S]: ").upper()
        player_2 = input("Player 2 choose [R-P-S]: ").upper()
        
        winner = compare (player_1, player_2)
        print(winner)
    
if __name__ == "__main__": main()