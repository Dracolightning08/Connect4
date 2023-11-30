import numpy as np
import pdb
import random
import utils
from copy import deepcopy

def get_computer_move(board, which_player):
    move = 4 #temporary
    depthlimit = 3
    validMoves = utils.get_valid_moves(board)
    print(validMoves)
    potentialActions = []
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        gameover, winner = playgame(newboard,which_player,validMoves[i]+1,0,depthlimit)
        potentialActions.append(winner)
    print(f"Potential Actions = {potentialActions}")
    
    #Below is shite. But it sorta works?
    goodActions = []
    opposition = (1 - which_player) + 1
    print(f"Player: {which_player}")
    print(f"Opposition: {opposition}")
    for i in range(len(potentialActions)):
        if potentialActions[i] != opposition:
            #print(i)
            if i in validMoves:
                goodActions.append(i+1)
    print(f"Good Actions: {goodActions}")
    if which_player+1 in potentialActions:
        move = potentialActions.index(which_player+1) + 1
    else:
        move = random.choice(goodActions)
    return move

def simulate_moves(board,player, col):
    #print(f"SIMULATION FOR {col}") #DEBUG
    #Updates the board
    col = col-1
    rows = utils.get_next_available_rows(board)
    row = rows[col]
    board[row][col] = player+1
    #print(board) #DEBUG
    #playgame(board,player,col, 1,1)
    return board

def playgame(board,player,col,depth,depthlimit):
    #print("NEW ITERATION OF PLAYGAME")
    board = simulate_moves(board,player,col)
    #Checks if game is over (does not check for DQ via Illegal Move)
    gameover, winner = utils.is_gameover(board)
    
    #print(f"Current Player: {player}")
    #print(board)
    #print(f"Game is over: {gameover}")
    #print(f"Winner: {winner}")
    
    #return imediately states:
    #if current state is a winner, return
    if gameover:
        return gameover, winner
    #if at the depth limit, return
    if depth == depthlimit:
        return gameover, winner
    
    #Go deeper actions
    validMoves = utils.get_valid_moves(board)
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        nextgameover, nextwinner = playgame(newboard, 1 - player, validMoves[i]+1, depth+1, depthlimit)
        #print(f"nextgameover = {nextgameover}")
        #print(f"nextwinner = {nextwinner}")

        #check if a later action was a victory for your opponent
        if nextgameover:
            #print(newboard)
            #print(f"Victory for {nextwinner} detected")
            #print("=============================================================================================================================")
            return nextgameover, nextwinner #temp, probably remove

    return nextgameover, nextwinner #temp, probably remove
    


