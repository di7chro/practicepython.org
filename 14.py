# practicepython.org
# Övning 14
#
# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing 
# a list, and another using sets.

def myRemoveDuplicates_1(startList):
    tempList = []
    for i in startList:
        if i not in tempList:
            tempList.append(i)
    return tempList

def myRemoveDuplicates_2(startList):
    return list(set(startList))

def main():
    startList = [1, 2, 2, 3, 3, 4, 5, 5, 6, 8, 8]
    
    print(startList)
    print(myRemoveDuplicates_1(startList))
    print(myRemoveDuplicates_2(startList))
if __name__ == "__main__": main()