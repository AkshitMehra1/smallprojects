from random import randint
repeat = True
print("Let's Begin")
while repeat:
    print("You rolled",randint(1,6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
