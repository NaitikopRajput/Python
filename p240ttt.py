l1=["0","1","2","3","4","5","6","7","8"]
print(l1)
t=1
while t<=9:
    if t%2==0:
        pos=int(input("Enter Position of O =>"))
        l1[pos]="O"
    else:
        pos=int(input("Enter Position of X =>"))
        l1[pos]="X"
    print(l1[0],"|",l1[1],"|",l1[2])
    
    print(l1[3],"|",l1[4],"|",l1[5])
   
    print(l1[6],"|",l1[7],"|",l1[8])
    
    t=t+1
    if l1[0] == "X" and l1[1] == "X" and  l1[2] == "X":
        print("X won the game !!!")
    elif l1[3] == "X" and l1[4] == "X" and  l1[5] == "X":
        print("X won the game !!!")
    elif l1[6] == "X" and l1[7] == "X" and  l1[8] == "X":
        print("X won the game !!!")
    elif l1[0] == "X" and l1[3] == "X" and  l1[6] == "X":
        print("X won the game !!!")
    elif l1[1] == "X" and l1[4] == "X" and  l1[7] == "X":
        print("X won the game !!!")
    elif l1[2] == "X" and l1[5] == "X" and  l1[8] == "X":
        print("X won the game !!!")
    elif l1[0] == "X" and l1[4] == "X" and  l1[8] == "X":
        print("X won the game !!!")
    elif l1[2] == "X" and l1[4] == "X" and  l1[6] == "X":
        print("X won the game !!!")


    if l1[0] == "O" and l1[1] == "O" and  l1[2] == "O":
        print("O won the game !!!")
    elif l1[3] == "O" and l1[4] == "O" and  l1[5] == "O":
        print("O won the game !!!")
    elif l1[6] == "O" and l1[7] == "O" and  l1[8] == "O":
        print("O won the game !!!")
    elif l1[0] == "O" and l1[3] == "O" and  l1[6] == "O":
        print("O won the game !!!")
    elif l1[1] == "O" and l1[4] == "O" and  l1[7] == "O":
        print("O won the game !!!")
    elif l1[2] == "O" and l1[5] == "O" and  l1[8] == "O":
        print("O won the game !!!")
    elif l1[0] == "O" and l1[4] == "O" and  l1[8] == "O":
        print("O won the game !!!")
    elif l1[2] == "O" and l1[4] == "O" and  l1[6] == "O":
        print("O won the game !!!")
    

