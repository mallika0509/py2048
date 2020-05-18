# py2048
Instructions: First enter the size of the matrix and amount needed to win. please enter only numbers.
if you enter a number that is not a power of 2, the winning quantity will be equal to the smallest power of 2 closest to entered value.
following this enter your move and press enter. 
w/W is up
s/S is down
a/A is left of user
d/D is right of user
if you enter a character other than the above mentioned ones, you will have to re-enter a valid move.
the moment winning quantity appears on the matrix,u win the game.
similarly, if the matrix if full of non-zero numbers before the winning amount appears, you will have lost the game.

[GAME WAS RUN ON WINDOWS IN COMMAND PROMPT USING SUBLIME TEXT]

The first few lines of the code, require the user to enter the desired size of matrix and the amount required to win.

printGame() is to create the initial matrix comprising zeroes and one random 2.

doubleH() is to double the values in horizontal direction. It works on the logic that if the adjacent element is equal to the previous one,
the previous one doubles and the adjacent element becomes zero to facilitate movement.

doubleV() does the same job but in the vertical direction.

moveH() is to move the elements of the matrix row by row towards the left such that all zeroes get pushed to the right. The logic used
here is that if the adjacent element is 0, the previous element takes its place and becomes 0 to facilitate further movement.

moveV() does the same job in the vertical direction

printM() is used to print the new matrix after every move

insert2() is used to insert 2 at a random position originally occupied by 0. It uses the randint() imported from random. variable n2=n*n 
because that is the maximum number of iterations required to find a spot occupied by 0 in the matrix.

askMove() is used to prompt the user to enter a move and accept it

checkWin() checks if the matrix contains the winning amount. if yes, it prints the corresponding message and exits the system.

checkLose() checks if all the positions of matrix are occupied. if yes, the user has lost the game

revH() inverts the matrix horizontally. Its requirements are discussed later

transpose() returns a matrix that is the transpose of the parameter matrix

checkMove(){recursive function} checks the entered move and performs the required action
a move: moveH fuction is called n times because that is the maximum number of iterations needed to push all the zeroes to the right. after that,
thedoubleH() is invoked and the moveH() is invoked again to cover up the zeroes formed after doubling.
d move: if the matrix is inverted horizontally the changes needed to successfully carry out the d move are the same as the a move. so after 
inverting and carrying out the required changes, it is inverted again to restore its original status
EG:-- 1002       2001       2100     0012
      1020       0201       2100     0012
      1001       1001       1100     0011
      2000       0002       2000     0002
w move: logic used is similar to that of the a move,but the row index is used here instead of the column index like in the a move.
s move: transposing a matrix, reversing it horizontally and transposing again, gives the original matrix in an
inverted form. operations similar to move w move are conducted and transposing-reversing-transposing is repeated.
invalid move: if the user enters any character other than a,w,s or d, it is said to be invalid. so the user has
been prompted to enter another move

if the user enters a number that is not a power of 2, that number will never appear on the game board. so according to
the instructions, given on the discord app, the winning quantity has to be changed to the power of 2 that is less than the entered number. 

if entered n is an unacceptable value, it has to be made to the default value=5.

finally, after printing the matrix, the code must check if the user has already won or lost and only then ask for a move
