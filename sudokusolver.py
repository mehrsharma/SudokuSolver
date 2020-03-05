# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Authored by: Mehr Sharma, Jay Bhagat


# SUDOKU SOLVER
# Rules:
# There must be a number in each space that follows the following rules:
# 1) Must be between 1 and 9 (inclusive)
# 2) All rows and columns can only have 1 of each number
# 3) Each 3x3 block can only have 1 of each number
# If you find numbers to fill each position such that the rules are fulfilled, you win!
# Change around the grid to solve your own Sudoku problem!

import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

#print(np.matrix(grid))

# single_num_checker(num_to_check, x, y) returns True if num_to_check is a
#   candidate for the position that is defined by (x, y) in Cartesian 
#   coordinates (i.e. if it follows the rules of Sudoku)
# requires: 0 < x, y < 9
#           1 <= num_to_check <= 9

def single_num_checker (y,x,num_to_check) :
    global grid
    
    #checking columns
    for i in range (0,9) :
        if grid[y][i] == num_to_check :
            return False
    
    #checking rows
    for i in range (0,9) :
        if grid [i][x] == num_to_check :
            return False
    
    #checking squares
    x0 = (x//3)*3
    y0 = (y//3)*3
    
    for i in range (0,3) :
        for j in range (0,3) :
            if grid[y0+i][x0+j] == num_to_check :
                return False
    
    return True

# solve() modifies grid to solve the Sudoku problem using single_num_checker
# effects: modifies grid
#          prints output
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for num in range (1,10) :
                    if single_num_checker(y,x,num):
                        grid[y][x] = num
                        #recursive step
                        solve()
                        #backtracking
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    
print(solve())



