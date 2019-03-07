import random
di={'r':"rock",'p':"paper",'s':"scissor"}
l=["r","p","s"]

cscore = 0
uscore = 0

while True:

    u = input("Enter your choice= ")
    print("  You choose: ",di[u])
    c = random.choice(l)
    print("  Computer chooses: ",di[c])
    if u == c:
        print("It's a tie")
    if c == 'r' and u == 's':
        print("C is the winner")
        cscore=cscore+1
    if c == 'r' and u == 'p':
        print("U is the winner")  
        uscore=uscore+1
    if c == 's' and u == 'p':
        print("C is the winner")
        cscore=cscore+1
    if c == 's' and u == 'r':
        print("U is the winner")
        uscore=uscore+1
    if c == 'p' and u == 's':
        print("U is the winner")
        uscore=uscore+1
    if c == 'p' and u == 'r':
        print("C is the winner")
        cscore=cscore+1


    print("\nScore is shown below: \n")
    print("Computer ",cscore,"\nUser     ",uscore)

    if cscore==3:
        print("Computer is a champ")
        
    elif uscore==3:
        print("You are a champ")
        exit()
