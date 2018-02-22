# practicepython.org
# Övning 15
#
# Write a program (using functions!) that asks the user for a long string containing 
# multiple words. Print back to the user the same string, except with the words in 
# backwards order. 
# For example, say I type the string:
#  My name is Michele
# Then I would see the string:
#   Michele is name My
# shown back to me.

def revString1(org):
    words = org.split()
    words.reverse()
    return " ".join(words)

def revString2(org):
    words = org.split()
    res = []
    for i in reversed(words):
        res.append(i)
    return " ".join(res)
    
def main():
    #test = input("Ange en sträng: ")
    test = "Kalle leker med elden"
    print (revString1(test))
    print (revString2(test))
    
if __name__ == "__main__": main()