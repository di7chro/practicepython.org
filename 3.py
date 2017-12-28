# practicepython.org
# Övning 3
# Take a list, say for example this one:
# myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# 1. Instead of printing the elements one by one, make a new list that has all the 
# elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# 2. Ask the user for a number and return a list that contains only elements from 
# the original list myList that are smaller than that number given by the user.

def main():
    myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    newList = []
    max_number = int (input("Ange största talet i nya listan: "))

    for index,number in enumerate(myList, start=0):
        if number <= max_number:
            print("{} på index {} är mindre än 5.".format(number, index))
            newList.append(number)
    print("Den nya listan innehåller: ", newList)
if __name__ == "__main__": main()