Project Title: Silly Name Generator
Project Objective: Make a program that generates funny aliases

Pseudocode
----------
Load a list of names
Load a list of surnames
Choose a first name at random
Assign the name to a variable
Choose a surname at random
Assign the name to a variable
Print the names to the screen in order and in red font
Ask the user to quit or play again
If user plays again:
	repeat
If user quits:
	end and exit
----------

The book points you to https://nostarch.com/impracticalpython/ for the code
and I am going to use it as a blueprint for my program. They reccomend using pylint
to parse the code and give a readibility check.

---------
SNGen.py before cleaning
---------
import sys, random

print("Welcome to the random name generator!\n")
print("A silly name for anyone:\n\n")

first = ('Big Nose', 'Jolly', 'Giga', 'Neighborly', 'Clean cut', 'Terryifying', 'Innocent')

last = ('Reindeer', 'Roger', 'Chad', 'Guy', 'Andy', 'Scarecrow', 'Debby')

while True:
    firstName = random.choice(first)
    
    lastName = random.choice(last)
    
    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")
    
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
-----------

Pylint points out that there is no docstrings present in the code and 
that every variable is defined as global. We can fix this by defining 
a main function and calling it with our code inside it. Using the built 
in variable __name__ we can set up an if statement to call our function.

----------
SNGen_clean.py
----------
"""
Generates funny sounding names by combining names from lists
and prints them to the screen with repeat functionality
"""
import sys
import random

def main():
    print("Welcome to the random name generator!\n")
    print("A silly name for anyone:\n\n")

    first = ('Big Nose', 'Jolly', 'Giga', 'Neighborly', 'Clean cut', 'Terryifying', 'Innocent')

    last = ('Reindeer', 'Roger', 'Chad', 'Guy', 'Andy', 'Scarecrow', 'Debby')

    while True:
        firstName = random.choice(first)
        
        lastName = random.choice(last)
        
        print("\n\n")
        print("{} {}".format(firstName, lastName), file=sys.stderr)
        print("\n\n")
        
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")   

if __name__ == "__main__":
    main()