# practicepython.org
# Övning 10
#
# Take two lists, say for example these two:
#    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:
# Generate 2 random lists and do the same

import random

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    temp = [i for i in a if i in b]
    result = []
    
    for num in temp:
        if num not in result:
            result.append(num)
    print("List A: ", a)
    print("List B: ", b)
    print("Gemensamma: ", result)

    rand1 = random.sample(range(1,30), 12)
    rand2 = random.sample(range(1,30), 16)
    rand1.sort()
    rand2.sort()
    
    temp = [i for i in rand1 if i in rand2]
    result = []
    
    for num in temp:
        if num not in result:
            result.append(num)
    print("\nRand 1: ", rand1)
    print("Rand 2: ", rand2)
    print("Gemensamma: ", result)
    
if __name__ == "__main__": main()