import numpy as np
import pdb
import random
import utils
from copy import deepcopy

def get_computer_move(board, which_player):
    move = 1 #temporary
    validMoves = utils.get_valid_moves(board)
    print(validMoves)
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        simulate_moves(newboard,which_player,validMoves[i]+1)
    print("After all that")
    print(board)
    return move

def simulate_moves(board,player, col):
    print(f"SIMULATION FOR {col}")
    #Updates the board
    col = col-1
    rows = utils.get_next_available_rows(board)
    row = rows[col]
    board[row][col] = player+1
    print(board)
    #Checks if game is over (does not check for DQ via Illegal Move)
    gameover, winner = utils.is_gameover(board)
    print(gameover)