# practicepython.org
# Övning 13
#
# Write a program that asks the user how many Fibonnaci numbers to generate 
# and then generates them. 
# Take this opportunity to think about how you can use functions.

def fibonacci(antal):
    i = 1
    if antal == 0:
        fib = []
    elif antal == 1:
        fib = [1]
    elif antal == 2:
        fib = [1, 1]
    elif antal > 2:
        fib = [1, 1]
        while i < (antal - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1   
    return fib

def main():
    try:
        antal = int(input("Hur många Fibonacci-nummer vill du ha? "))
    except ValueError:
        print("Du måste ange en siffra")
    else:
        fib = fibonacci(antal)
        print(fib)
if __name__ == "__main__": main()