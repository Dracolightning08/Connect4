import numpy as np
import pdb
import random
import utils

def get_computer_move(board, which_player):
    #print(utils.get_next_available_rows(board))
    move = 1
    simulate_moves(board,which_player,move)
    return move

def simulate_moves(board,player, col):
    print("SIMULATION")
    #Updates the board
    col = col-1
    rows = utils.get_next_available_rows(board)
    row = rows[col]
    board[row][col] = player+1
    print(board)
    #Checks if game is over (does not check for DQ via Illegal Move)
    gameover, winner = utils.is_gameover(board)
    print(gameover)