#!/usr/bin/python3
from square_utils import *


def valid(board):
    return row_check(board) and col_check(board) and angle_check(board)


def get_pos(board):
    return list(set(range(1, 10)) - set(board))


def stack_burn(board, stack_must_ret):
    board.pop()
    while not stack_must_ret[-1]:
        stack_must_ret.pop()
        if len(board) == 0:
            exit(0)
        board.pop()
    board.append(stack_must_ret[-1].pop())
    return board, stack_must_ret


work = []
stack = []
# while the solutions space is not fully explored
while True:
    # Complete
    if len(work) == 9:
        # Correct
        if len(work) == 9 and valid(work):
            print("Valid: " + str(work))
            # Optimal
            if False:
                pass
        work, stack = stack_burn(work, stack)
    elif valid(work):
        if len(stack):
            stack.append(get_pos(work))
        else:
            stack = [get_pos(work)]
        work.append(stack[-1].pop())
    else:
        work, stack = stack_burn(work, stack)
