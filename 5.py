# practicepython.org
# Övning 5
#
# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the 
# elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:
# Randomly generate two lists to test this

from random import randint

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print("Lista A: ", a)
    print("Lista B: ", b)

    common_a_b = list(set(a) & set(b))          # Skapa lista med gemensamma tal
    print("Gemensamma element: ", common_a_b)
    
    # Skapa två listor att fylla med slumptal 
    random_list_a = []
    random_list_b = []
    
    # Fyll listorna med slump-siffror
    for _ in range (randint(10, 20)):           # Listans storlek är slumpad (10-20)
        random_list_a.append(randint(1, 20))    # Talen slumpas mellan (1-20)
    for _ in range (randint(10, 20)):
        random_list_b.append(randint(1, 20)) 

    print("\nLista A: ", random_list_a)
    print("Lista B: ", random_list_b)

    common_rand_lists = list(set (random_list_a) & set(random_list_b))  # Skapa lista med gemensamma tal
    common_rand_lists.sort();                   # Sortera talen i listan
    print("Gemensamma element: ", common_rand_lists)
if __name__ == "__main__": main()
