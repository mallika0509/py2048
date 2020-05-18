from random import randint#used to generate random index values for 2
import sys#used to exit game after winning or losing
print('Welcome!!')
n=input('Enter the number of desired rows and columns: ')
n=int(n)
winTemp=input('Enter the amount needed to win: ')
winTemp=int(winTemp) 
matrix=[]

def printGame(n,w):#used to print starting matrix
    for i in range(n):#line11-15: to create an n*n matrix of zeroes                                                                                                                                                                                                               
        a =[] 
        for j in range(n):      
             a.append(int(0)) 
        matrix.append(a) 
    r1=randint(0,n-1)#line16-18: to insert 2 at a random position
    r2=randint(0,n-1)
    matrix[r1][r2]=2
    for i in range(n):#line19-22: to print matrix
        for j in range(n): 
            print(matrix[i][j], end = " ") 
        print()

def doubleH(matrix1):
#function used to double the values if equal numbers are adjacent to each other in horizontal direction
    for i in range(n): 
        for j in range(n-1): 
            if matrix1[i][j]==matrix1[i][j+1]:
                matrix1[i][j]=2*matrix1[i][j+1]
                matrix1[i][j+1]=0
    return matrix1

def doubleV(matrix1):
#function used to double the values if equal numbers are adjacent to each other in vertical direction
    for j in range(n): 
        for i in range(n-1): 
            if matrix1[i][j]==matrix1[i+1][j]:
                matrix1[i][j]=2*matrix1[i+1][j]
                matrix1[i+1][j]=0
    return matrix1

def moveH(matrix1):
#function used to move numbers towards the right and eliminate zeroes between non-zero numbers
    for i in range(n): 
            for j in range(n-1): 
                if matrix1[i][j]==0:
                    matrix1[i][j]=matrix1[i][j+1]
                    matrix1[i][j+1]=0
    return matrix1

def moveV(matrix1):
#function used to move numbers upwards and eliminate zeroes between non-zero numbers
    for j in range(n): 
        for i in range(n-1): 
            if matrix1[i][j]==0:
                matrix1[i][j]=matrix1[i+1][j]
                matrix1[i+1][j]=0 
    return matrix1

def printM(matrix1,n):
#function used to print matrix after every move
    for i in range(n): 
        for j in range(n): 
            print(matrix1[i][j], end = " ") 
        print()

def insert2(matrix2):
#function used to insert 2 at random position where zero was initially present
    n2=n*n
    for k in range(n2):
        i=randint(0,n-1)
        j=randint(0,n-1)
        if matrix2[i][j]==0:
            matrix2[i][j]=2
            break
    return matrix2    

def askmove():
#function used to prompt user to enter a move and accept it
    move=input('Enter your move: ')
    return move

def checkWin(matrix1,n,w):
#function used to check if the user has won by checking if any 
#of the numbers in the matrix matches the winning amount
    count=0
    for i in range(n):
        for j in range(n):
            if matrix1[i][j]==w:
                print("congratulation!! you won")
                count=1
                sys.exit()
                break
    if count==0:
        move=askmove()
        return move

def checkLose(matrix):
#function used to check if the user has lost by checking if all entries in matrix are full
    count=0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==0:
                count=1
                break
    if count==0:
        print("Sorry!! You lost.")
        sys.exit()

def revH(matrix):
#function used to create a matrix that is a mirror image of the previous one such 
#that mirror is on the right
    new=[]
    for k in matrix:
        k.reverse()
        new.append(k)
    return new

def transpose(a,n):
#function used to create a transpose matrix
    b=[]
    for i in range(n): 
        dummy=[]
        for j in range(n): 
            dummy.append(a[j][i])
        b.append(dummy)
    return b

def checkMove(move,matrix,n):
    #w is up
    #s is down
    #a is left of player
    #d is right of player
    if move=='a':
        matrix=doubleH(matrix)
        for k in range(0,n):
            matrix=moveH(matrix)
        matrix=doubleH(matrix)
        matrix=insert2(matrix)
        printM(matrix,n)
        checkLose(matrix) 
        move=checkWin(matrix,n,w)
        checkMove(move,matrix,n)
    elif move=='d':
#for the right move, the matrix is first inverted horizontally and moves 
#identical to the a move are applied and to get back the original matrix 
#it is inverted again horizontally
        matrix=revH(matrix)
        matrix=doubleH(matrix)
        for k in range(0,n):
            matrix=moveH(matrix)
        matrix=doubleH(matrix)
        matrix=revH(matrix)
        matrix=insert2(matrix)
        printM(matrix,n)
        checkLose(matrix)
        move=checkWin(matrix,n,w)
        checkMove(move,matrix,n)
    elif move=='w':
        matrix=doubleV(matrix)
        for k in range(0,n):
            matrix=moveV(matrix)
        matrix=doubleV(matrix)
        matrix=insert2(matrix)
        printM(matrix,n)
        checkLose(matrix)
        move=checkWin(matrix,n,w)
        checkMove(move,matrix,n)
    elif move=='s':
#by transposing the matrix, inverting it horizontally and transposing it again,
#a matrix that is the mirror image of the previous one in the downward direction
#is obtained. moves identical to w move are made and same process of 
#transposing-inverting-transposing is conducted to restore original matrix
        matrix=transpose(matrix,n)
        matrix=revH(matrix)
        matrix=transpose(matrix,n)
        matrix=doubleV(matrix)
        for k in range(0,n):
            matrix=moveV(matrix)
        matrix=doubleV(matrix)
        matrix=transpose(matrix,n)
        matrix=revH(matrix)
        matrix=transpose(matrix,n)
        matrix=insert2(matrix)
        printM(matrix,n)
        checkLose(matrix)
        move=checkWin(matrix,n,w)
        checkMove(move,matrix,n)
    else:#if move entered is invalid the user must be asked to enter another move
        print("invalid move")
        move=askmove()
        checkMove(move,matrix,n)

#line198-203: if a user enters a value that is not a power of 2,
#the winning value should be made to the highest power of 2 lying 
#in the interval(-infinity,entered value]. Also if a number lower
#than 2 is entered, winning value must be made to default value(2048)
if winTemp<2:
    w=2048
winNum=[2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072]
for k in range(0,16):
    if winTemp>=winNum[k] and winTemp<winNum[k+1]:
        w=winNum[k]

print("number needed to win is: "+str(w))      

#line 209-212: if n entered is less than equal to zero, value of n 
#must be put equal to 5(default)
if n>0:
    printGame(n,w)    
else:
    printGame(5,w)

checkLose(matrix)#if n=1, and w not equal to 2, the user has lost 
#in the first move itself. so a check has been put
move=checkWin(matrix,n,w)# similarly, if w=2, the user has won already
#so a check has been put
checkMove(move,matrix,n)