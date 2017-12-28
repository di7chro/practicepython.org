# practicepython.org
# Övning 7
#
# Let’s say I give you a list saved in a variable: 
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list and makes a new list that 
# has only the even elements of this list in it.

from random import randint

def generate_random_list():
    random_list = []
    for _ in range (randint(10, 20)):       # Listans storlek är slumpad (10-20)
        random_list.append(randint(1, 20))  # Talen slumpas mellan (1-20)
    return random_list

def main():
    my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [number for number in my_list if number%2 == 0]
    print("Bara jämna tal i listan: ", even_list)
    
    random_list = generate_random_list()
    new_list = [number for number in random_list if number%2 == 0]
    new_list.sort()
    print("Bara jämna tal i slump-listan: ", new_list)
if __name__ == "__main__": main()