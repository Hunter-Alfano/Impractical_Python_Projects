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