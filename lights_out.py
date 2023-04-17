# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:11:27 2021

@author: Jackson
"""
import random
def main():
    board = [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]
    randomize(board)    
    #1 is lights out
    #0 is lights on  
    moves = 0
    while(solved(board) == False):
        #loops until solved() returns True
        display(board)
        row = int(input("Input your desired row, 0-4: "))
        column = int(input("Input your desired column, 0-4: "))
        #user input for row and column
        board = play(board,row,column)
        #calls on play function
        moves+=1
    print("You won with", moves, "moves!")

def display(board):
    x = '\u25a1'
    y = '\u25a0'
    #this creates the cubes x is for light cubes, y is for dark cubes
    line = ""
    #line will create a string of each row and print them 1 at a time(just for format)
    for row in range(5):
        
        line = ""
        for col in range(5):
            value = board[row][col]
            if(value == 0):
                line+=" "
                #I have to add in this space because if not the cubes merge together
                line+=y
            if (value == 1):
                line+=" "
                line+=x
        print(line)

def play(board,row,column):
    above = int(row) - 1
    below = int(row) + 1
    left = int(column) - 1
    right = int(column) + 1
    #above calculates the position of the 4 other places where
    #the lights would change in addition to center
    avaliable = ["above","below","left","right","center"]
    if (above < 0 or above > 4):
        avaliable.remove("above")
    if (below < 0 or below > 4):
        avaliable.remove("below")
    if (left < 0 or left > 4):
        avaliable.remove("left")
    if (right < 0 or right > 4):
        avaliable.remove("right")
    #above removes any of the 4 possible changes if they are out of range of the board
    if("center" in avaliable):        
        board[row][column] = getCenter(board,row,column)
        #had to create getCenter() because of unknown issue, simply changes either on or off
        
    if("above" in avaliable):
        value = board[above][column]
        if(value == 0):
            board[above][column] = 1
        else:
            board[above][column] = 0
            
            
    if("below" in avaliable):
        value = board[below][column]
        if(value == 0):
            board[below][column] = 1
        else:
            board[below][column] = 0
            
            
    if("left" in avaliable):
        value = board[row][left]
        if(value == 0):
            board[row][left] = 1
        else:
            board[row][left] = 0
            
            
    if("right" in avaliable):
        value = board[row][right]
        if(value == 0):
            board[row][right] = 1
        else:
            board[row][right] = 0
    #above changes the avaliable positions on the board either from on to off
    return board
            
def solved(board):
    solved_board = [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]             
    if(board == solved_board):
        return True
    #return true if current board matches solved board
    else:
        return False
    
def randomize(board):
    numberOfMixes = random.randint(10,100)
    #number of times board will be mixed
    for x in range(numberOfMixes):
        row = random.randint(0,4)
        column = random.randint(0,4)
        play(board,row,column)
        #calls on play() in order to randomize the board a random number of times
    return board
    
    
def getCenter(board,row,column):
    if(board[row][column] == 1):
        value = 0
        #returns either a 1 or 0, will always be the oposite of what comes in
    else:
        value = 1
    return value
    



main()