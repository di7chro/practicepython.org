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

def main():
    print("Rock Paper Scissors")
    print("Regler:")
    print("# [R]ock beats scissors")
    print("# [S]cissors beats paper")
    print("# [P]aper beats rock")

    player_1 = input("Spelare 1's väljer [R-P-S]: ")
    player_2 = input("Spelare 2's väljer [R-P-S]: ")
    # NOT DONE!
if __name__ == "__main__": main()