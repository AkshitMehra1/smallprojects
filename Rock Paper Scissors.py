import random
lst=['rock','paper','scissors']
computer = random.choice(lst)
print("Enter your choice")
print("1- Start")
print("2- Stop")
i=int(input())
cs, us=0,0
while i==1:
    print("Choose from rock, paper and scissors")
    user=input()
    print("The computer chose " + computer)
    if user=='rock':
        if computer=="paper":
            print("Computer Wins")
            cs+=1
        elif computer=="rock":
            print("Nobody Wins")
        else:
            print("User Wins")
            us+=1
    elif user=="paper":
        if computer=="scissors":
            print("Computer Wins")
            cs+=1
        elif computer=="paper":
            print("Nobody Wins")
        else:
            print("User Wins")
            us+=1
    elif user=="scissors":
        if computer=="rock":
            print("Computer Wins")
            cs+=1
        elif computer=="scissors":
            print("Nobody Wins")
        else:
            print("User Wins")
            us+=1
    else:
        print("The user has to chose from rock, paper and scissors only")
    print("Enter 1 to play more and any other number to leave")
    i=int(input())
print("The final score is Computer - User")
print(cs,"-",us)