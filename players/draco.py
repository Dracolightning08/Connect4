import pdb
import random
import utils
import queue
import math
from copy import deepcopy


def fake_drop(board, player, col):
    # print(f"SIMULATION FOR {col}") #DEBUG
    # Updates the board
    col = col - 1
    rows = utils.get_next_available_rows(board)
    row = rows[col]
    board[row][col] = player + 1
    # print(board) #DEBUG
    # playgame(board,player,col, 1,1)
    return board


def redo(board, curPlayer, originalPlayer, firstMove=-1, alpha=-math.inf, beta=math.inf, depth=0):
    maxHeuristic = -1
    bestMove = -1
    for move in utils.get_valid_moves(board):
        # print(move)
        newBoard = fake_drop(board, curPlayer, move + 1)
        # print("A")
        h = heuristic(newBoard, curPlayer)
        # print(h)
        if (h > maxHeuristic):
            bestMove = move
            maxHeuristic = h
    return bestMove + 1


def checkCount(direction, board, row, col, player):
    # Possible Directions: L, R, U, D, and any combination of L/R and U/D
    # Returns number of pieces in the possible row
    rowMove = 0

    colMove = 0

    if "L" in direction:
        rowMove = -1
    elif "R" in direction:
        rowMove = 1
    if "U" in direction:
        colMove = 1
    elif "D" in direction:
        colMove = -1
    newRow = row + rowMove
    newCol = col + colMove
    # print("Col", type(len(board[0])))
    count = 0
    score = 0
    verbose = False
    while (newCol < len(board[0])
           and newRow < len(board)
           and newCol > 0
           and newRow > 0
           and count < 4):
        verbose = False
        if direction == "R":
            verbose = True
        if (board[newRow][newCol] == player + 1):

            if verbose: print("Score increase", score)
            score += 1
        elif (board[newRow][newCol] != 0):
            if verbose:
                print(board[newRow][newCol])
                print(newRow, newCol)

            # If the next piece is not 0 set score to 0 and break out
            # This is not a possible row
            score = 0
            break
        newCol += colMove
        newRow += rowMove
        count += 1
    if count != 4:

        if verbose:
            print("Didn't make it to the end")
            print(count)
        score = 0  # Getting 4 is out of range so no score associated
    return score


def heuristic(board, player):
    possibleMoves = ("L", "R", "U", "D", "LU", "LD", "RU", "RD")
    # Need to find how big of a threat any particular move is
    # For now im picking a random
    # print(player + 1)
    playerItems = []
    # print(board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            # print(row, col)
            if board[row][col] == player + 1:
                playerItems.append((row, col))

                # print("Found a player item")
    maxScore = 0
    for row, col in playerItems:
        for move in possibleMoves:
            # print(move)
            score = checkCount(move, board, row, col, player)
            if score > maxScore:
                maxScore = score
    print(maxScore)
    return maxScore


def get_computer_move(board, which_player):
    return redo(board, which_player, which_player)