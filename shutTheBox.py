#! /usr/bin/python3

import random
import sys #to trigger game over for incorrect input
import time
import itertools #to calculate all possible play comibinations based on available board integers

#setting up the Board to show which number slot we're in, which will have an integer
#until it is selected by the user to be removed from the board, then it will be 'X'



theBoard = [1, 2, 3, 4,\
            5, 6, 7, 8, 9, \
            10]

## Need to add """ """ notation to functions

#defining function for the visual of the board, starts with showing each integer 1 thru 10
def printBoard(board):
    print(str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|' \
          + str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]) + '|' \
          + str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]) + '|' \
          + str(board[9]) + '|')


#function to check if game has been won, need to expand on this to give the option to start a new game
def winCon():
    winTotal = 0
    if theBoard == ['X', 'X', 'X','X',\
            'X', 'X', 'X', 'X', 'X', \
            'X']:
        print('Congratulations, you\'ve won!')
        winTotal += 1
        print('You\'ve won ' + str(winTotal) + ' games.')
    

def newGame():
    while True:
        print('Would you like to start a new game?  y/n?')
        response = input()
        if response == 'n':
            print('Goodbye!')
            sys.exit()
        if response == 'y':
            diceRollFunc()
        else:
            continue
    

    

#function to show all available plays, using itertools module
#def combos():
    
            

def diceRollFunc():
    theBoard = [1, 2, 3, 4,\
            5, 6, 7, 8, 9, \
            10]
    while theBoard != ['X', 'X', 'X','X',\
            'X', 'X', 'X', 'X', 'X', \
            'X']:
        diceRoll = random.randint(1, 6) + random.randint(1,6)
        while True:
            print('Roll the pair of dice by typing \'r\'.')
            roll = input()
            if roll == ('r'):
                print('You rolled a ' + str(diceRoll) + '.  Now choose which \
numbers to remove from the board.')
                print('Here\'s the board again, enter one number \
at a time to remove it from the board.')
            printBoard(theBoard)
            print('Here are your available plays.')
            availablePlay = []   #empty list that will then populate with current integers on the board
            for i in theBoard[:10]:  #iterate through the board,  creating a new list to remove all "X' and keep only integers
                try:
                    
                    if i == 'X':
                        continue
                    else:
                        availablePlay.append(i)
                        
                except ValueError:
                    continue
                except TypeError:
                    continue
                
            result = [seq for i in range(len(availablePlay), 0 , -1) for seq in itertools.combinations(availablePlay, i) if sum(seq) == diceRoll]  #itertools sequence to create list variable containing all available plays
            if result == []:
                print('You have none. Game over.')
                
                newGame()
            else:
                print(result)
            newBoard = input()
            newBoard1 = 0
            newBoard2 = 0
            newBoard3 = 0
            try:
                if int(newBoard) != int(theBoard[int(newBoard)-1]):   #test to check if input is an available space on board and not already an 'X'
                    continue
            except ValueError:
                print('That is an invalid input, start over.')
                newGame()
            except IndexError:
                print('That is an invalid input, start over.')
                newGame()
            if int(newBoard) > 0 and int(newBoard) < 11 and int(newBoard) <= diceRoll:
                theBoard[int(newBoard)-1] = 'X'
            if (int(diceRoll) - int(newBoard)) == 0:
                break
            if int(newBoard) > int(diceRoll):
                print('That is an invalid input, start over.')
                newGame()
            if (int(diceRoll) - int(newBoard)) != 0:
                print('Please enter another number to remove')
                newBoard1 = input()
                theBoard[int(newBoard1)-1] = 'X'
            if (int(newBoard1) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                newGame()
            if (int(diceRoll) - int(newBoard) - int(newBoard1)) == 0:
                break
            if (int(diceRoll) - int(newBoard) - int(newBoard1)) != 0:
                print('Please enter another number to remove')
                newBoard2 = input()
                theBoard[int(newBoard2)-1] = 'X'
            if (int(newBoard1) + int(newBoard2) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                newGame()
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2)) == 0:
                break
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2)) != 0:
                print('Please enter another number to remove')
                newBoard3 = input()
                theBoard[int(newBoard3)-1] = 'X'
            if (int(newBoard1) + int(newBoard2) + int(newBoard3) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                newGame()
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2) - int(newBoard3)) == 0:
                break
            
            #Need to define function or statement that will check if current dice roll is playable on the available board integer spaces in the list, if not, the game needs to end.
            
        printBoard(theBoard)
        
        




print('Welcome to Shut the Box! Here is your board, let\'s get started.')


printBoard(theBoard)

diceRollFunc()


       
winCon()
