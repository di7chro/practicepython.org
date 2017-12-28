# practicepython.org
# Övning 4
#
# Create a program that asks the user for a number and then prints out a 
# list of all the divisors of that number. 
# If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def main():
    number = int (input ("Ange ett tal: "))
    divider_list = []
    for divider in range(1, number):
        if number % divider == 0:
            divider_list.append(divider)
    if len(divider_list) == 1:
        print("Talet {} är ett primtal.".format(number))
    else:
        print("Alla delare till talet: ", divider_list)
if __name__ == "__main__": main()