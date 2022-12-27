#!/usr/bin/python

def row_check(board):
    return (len(board) < 3 or sum(board[0:3]) == 15 and
            len(board) < 6 or sum(board[3:6]) == 15 and
            len(board) < 9 or sum(board[6:9]) == 15)


def col_check(board):
    return ((len(board) < 7 or (board[0] + board[3] + board[6]) == 15) and
            (len(board) < 8 or (board[1] + board[4] + board[7]) == 15) and
            (len(board) < 9 or (board[2] + board[5] + board[8]) == 15))


def angle_check(board):
    return ((len(board) < 9 or (board[0] + board[4] + board[8]) == 15) and
            (len(board) < 7 or (board[2] + board[4] + board[6]) == 15))
