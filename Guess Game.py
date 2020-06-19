import random
print("You have to guess a number between 1-20.\nYou will have 3 chances.\nAfter each turn the computer will tell you whether you are correct, higher than the number or lower than the number.")
comp=random.randint(1,20)
print("Enter\n1-Play\n2-Stop")
i=int(input())
user,tme,score=0,0,0
while i==1:
    print("Enter the number")
    user=int(input())
    if user==comp:
        print("You are correct")
        tme=0
        score+=1
    elif user>20 or user<=0:
        print("Enter between 1-20")
    elif user<comp:
        print("The number is higher than {}".format(user))
        tme+=1
        print("Your turns remaining are", 3-tme)
    elif user>comp:
        print("The number is lower than {}".format(user))
        tme+=1
        print("Your turns remaining are", 3-tme)
    if tme==3:
        print("The correct answer was {}".format(comp))
        print("Sorry you lost this game")
        print("Enter 1 to play again")
        i=int(input())
    elif tme==0:
        print("Enter 1 to play again")
        i=int(input())
print("Your score is", score)
