#This game will not have O and X but it will have 1 and 2 instead of them.
print("This game will be of 1 and 2 in tic tac toe" )
winner=3
game=0
a=[[0 for j in range (0,3)]for i in range(0,3)]
print(a)
while game==0: 
    print("Enter the row and then the column in which you want to add player" , winner-2)
    rowin=int(input())
    colin=int(input()) 
    rowin=rowin-1
    colin=colin-1
    if a[rowin][colin]!=0:
        print("Wrong Move!! Try again!")
        continue
    elif winner==3:
        a[rowin][colin]=1
    elif winner==4:
        a[rowin][colin]=2
    i=0
    j=0
    print("The new screen is")
    print(a)
    if a[0][0]==a[0][1]==a[0][2]==1 or a[0][0]==a[0][1]==a[0][2]==2:
        winner=a[0][0]
        break
    elif a[1][0]==a[1][1]==a[1][2]==1 or a[1][0]==a[1][1]==a[1][2]==2:
        winner=a[1][0]
        break
    elif a[2][0]==a[2][1]==a[2][2]==1 or a[2][0]==a[2][1]==a[2][2]==2:
        
        winner=a[2][0]
        break
    elif a[0][0]==a[1][0]==a[2][0]==1 or a[0][0]==a[1][0]==a[2][0]==2:
        winner=a[0][0]
        break
    elif a[0][1]==a[1][1]==a[2][1]==1 or a[0][1]==a[1][1]==a[2][1]==2:
        winner=a[0][1]
        break
    elif a[0][2]==a[1][2]==a[2][2]==1 or a[0][2]==a[1][2]==a[2][2]==2:
        winner=a[0][2]
        break
    elif a[0][0]==a[1][1]==a[2][2]==1 or a[0][0]==a[1][1]==a[2][2]==2:
        winner= a[0][0]
        break
    elif a[0][2]==a[1][1]==a[2][0]==1 or a[0][2]==a[1][1]==a[2][0]==2:
        winner=a[1][1]
        break
        
    if winner==3:
        winner=4
    elif winner==4:
        winner=3
    game=0
    
print("The winner is Player", winner)
    
