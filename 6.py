# practicepython.org
# Övning 6
# 
# Ask the user for a string and print out whether this string is a 
# palindrome or not. 
# A palindrome is a string that reads the same forwards and backwards.

# Reverserar en text med en loop
def reverse_slowly (text):
    new_string = ''
    index = len(text)
    while index:
        index -= 1                  # Hoppa till tecknet före
        new_string += text[index]   # Lägg in tecknet i nya strängen
    return new_string

# Reverserar en text med den inbyggda slice-funktionaliteten
def reverse_slice (text):
    return text[::-1]

def main():
    text = input("Ange en textsträng: ")
    rev_slow = reverse_slowly(text)
    if rev_slow == text:
        print("Detta är ett Palindrom")
    else:
        print("Nope, det är INTE ett Palindrom")
   
    rev_slice = reverse_slice(text)
    if rev_slice == text:
        print("Detta är ett Palindrom")
    else:
        print("Nope, det är INTE ett Palindrom")
    
if __name__ == "__main__": main()