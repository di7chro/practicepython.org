# practicepython.org
# Övning 11 
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

def main():
    a = [5, 10, 15, 20, 25]
    new_list = []
    new_list.append(a[0])
    new_list.append(a[len(a)-1])
    
    print("Nya listan med första och sista elementet: ", new_list)
if __name__ == "__main__": main()