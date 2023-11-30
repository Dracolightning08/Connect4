import numpy as np
import pdb
import random
import utils
from copy import deepcopy

def get_computer_move(board, which_player):
    #print(utils.get_next_available_rows(board))
    move = 1
    validMoves = utils.get_valid_moves(board)
    #simulate_moves(board,which_player,move)
    print(validMoves)
    print(f"I am player {which_player}")
    # board[0][4] = 1
    # print(board)
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        simulate_moves(newboard,which_player,validMoves[i]+1)
    # print("After all that")
    # print(board)
    return move

def simulate_moves(board,player, col):
    print(f"SIMULATION FOR {col}")
    #Updates the board
    col = col-1
    rows = utils.get_next_available_rows(board)
    print(rows)
    row = rows[col]
    board[row][col] = player+1
    print(board)
    playgame(board,player,1,1)
    return board

def playgame(board,player,depth,depthlimit):
    #Checks if game is over (does not check for DQ via Illegal Move)
    gameover, winner = utils.is_gameover(board)
    print(f"Game is over: {gameover}")
    print(f"Winner: {winner}")
    
    #return imediately states:
    #if current state is a winner, return
    if gameover:
        return gameover, winner
    #if at the depth limit, return
    if depth == depthlimit:
        return gameover, winner
    

