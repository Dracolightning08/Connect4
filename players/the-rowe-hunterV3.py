import numpy as np
import pdb
import random
import utils
from copy import deepcopy

def get_computer_move(board, which_player):
    depthLimit = 3 #3 for best performance
    whoAmI = which_player
    move = 1 #temp
    validMoves = utils.get_valid_moves(board) #List of all moves that are possible
    outcomes = []
    bestOutcome = -1
    #get a set of outcomes
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        searchResult = search(newboard,which_player,whoAmI,validMoves[i]+1,0,depthLimit)
        bestOutcome = max(bestOutcome,searchResult)
        outcomes.append(searchResult)
    
    #get the index of the best outcome
    print(validMoves)
    print(outcomes)
    print(bestOutcome)

    # if bestOutcome > 1:
    #     move = outcomes.index(bestOutcome) + 1
    # else:
    #     move = random.choice(validMoves) + 1
    
    return chooseFinalMove(validMoves,outcomes,bestOutcome)
    """
    KEY TO SEARCH RESULTS:
    -1: Nonterminal Node (if this returns, something is bugged in the code)
    0: Winner Uncertain (choose only if no win path is known yet)
    1: Opponent Victory (do not select)
    2+: Our Victory (higher numbers signify closer victories and should be prioritised)
    """

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

def checkForEndstate(board, player, whoAmI, depth, depthLimit):
    #print(board)
    if depth == depthLimit: #If at the depth limit, return DL
        return 0
    gameover, winner = utils.is_gameover(board)
    if gameover: #If the game has ended (Win, Loss, or Draw)
        whoAmI = whoAmI+1 #Update to match whinner results
        if winner == whoAmI: #if we win
            return 1 + (depthLimit-depth) #min of 2, has closer wins prioritised
        else:
            return 1 #Draws count as a loss
    return -1 #If not win, loss/draw, or depth limit (should continue).

def search(board, player, whoAmI, col, depth, depthLimit):
    board = simulate_moves(board,player,col)
    outcomeAtState = checkForEndstate(board,player,whoAmI,depth,depthLimit)
    
    if outcomeAtState != -1:  #Reached a terminal point
        return outcomeAtState
    
    #if not at terminal state, we need to go deeper
    validMoves = utils.get_valid_moves(board)
    bestOutcome = -1
    for i in range(len(validMoves)):
        newboard = deepcopy(board)
        bestOutcome = max(bestOutcome,search(newboard,1-player,whoAmI,validMoves[i]+1,depth+1,depthLimit))
    return bestOutcome #temp, shoud not be outcomeAtState

def chooseFinalMove(validMoves,outcomes,bestOutcome):
    if bestOutcome > 1: #A win path is known
        move = outcomes.index(bestOutcome) + 1
    else: #select any valid move not resuting in a win for opponent
        safeMoves = []
        for i in range(len(validMoves)):
            if outcomes[i] != 1 and outcomes[i] in validMoves: #if the outcome is not an opponent victory
                safeMoves.append(i)
        move = random.choice(safeMoves) + 1
    #print(safeMoves)
    
    return move