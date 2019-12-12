#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import time



class Struct():
    """Defines a dictionary with the 3X3 blocks for each cell based on flat index"""

    #Initialize the variables with the values for each cell in a flat array with 81 comp
    data_val = {}
    #######>>>>>>>>>Row 0>>>
    data_val[0] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[1] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[2] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    #####
    data_val[3] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[4] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[5] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    ###
    data_val[6] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[7] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[8] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    ###>>>>>>>>>>Row 1
    data_val[9] =  {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[10] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[11] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    #####
    data_val[12] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[13] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[14] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    ###
    data_val[15] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[16] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[17] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 2
    data_val[18] =  {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[19] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    data_val[20] = {'blk_row':slice(0,3),'blk_col':slice(0,3)}
    #####
    data_val[21] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[22] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    data_val[23] = {'blk_row':slice(0,3),'blk_col':slice(3,6)}
    ###
    data_val[24] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[25] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}
    data_val[26] = {'blk_row':slice(0,3),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 3
    data_val[27] =  {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[28] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[29] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    #####
    data_val[30] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[31] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[32] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    ###
    data_val[33] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[34] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[35] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 4
    data_val[36] =  {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[37] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[38] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    #####
    data_val[39] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[40] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[41] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    ###
    data_val[42] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[43] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[44] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 5
    data_val[45] =  {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[46] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    data_val[47] = {'blk_row':slice(3,6),'blk_col':slice(0,3)}
    #####
    data_val[48] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[49] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    data_val[50] = {'blk_row':slice(3,6),'blk_col':slice(3,6)}
    ###
    data_val[51] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[52] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}
    data_val[53] = {'blk_row':slice(3,6),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 6
    data_val[54] =  {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[55] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[56] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    #####
    data_val[57] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[58] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[59] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    ###
    data_val[60] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[61] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[62] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 7
    data_val[63] =  {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[64] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[65] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    #####
    data_val[66] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[67] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[68] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    ###
    data_val[69] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[70] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[71] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}

    ###>>>>>>>>>>Row 8
    data_val[72] =  {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[73] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    data_val[74] = {'blk_row':slice(6,9),'blk_col':slice(0,3)}
    #####
    data_val[75] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[76] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    data_val[77] = {'blk_row':slice(6,9),'blk_col':slice(3,6)}
    ###
    data_val[78] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[79] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    data_val[80] = {'blk_row':slice(6,9),'blk_col':slice(6,9)}
    
    def __init__(self):
        pass
    @classmethod
    def get_2D_blk(cls,i,j):
        """Get the 2D data for a block that belongs to the (i,j) tuple
           Input is i,j coordinates for row and column
           Output is the slice coordinates for the 3X3 block
        """
        arr = np.array([[i],[j]])
        flat_idx = np.ravel_multi_index(arr,(9,9))
        return (Struct.data_val[flat_idx[0]]['blk_row'],Struct.data_val[flat_idx[0]]['blk_col'])
        

def find_next_cell(grid):
    """Find next cell to be filled row by row"""

    for indx,v in np.ndenumerate(grid):
        if not v:
            return (indx[0],indx[1]) 
    return (-1,-1)
        
def is_valid(grid,i,j,e):
    """ Check if this value e is Sudoku valid in position i,j"""
    col = j
    row = i
    brow,bcol = Struct.get_2D_blk(i,j)
    comb = set(grid[:,col]).union(set(grid[row]),set(grid[brow,bcol].flat))
    if e in comb:
        return False
    else:
        return True
    
def sudoku_validate(grid):
    """
    check if the initial data is valid
    if there is an input value > 0:
    check if the column is unique
    check if the row is unique
    check if the square(3X3) is unique
    Input is 9X9 numpy array 
    """
    for ind,val in np.ndenumerate(grid):
        if val:
            col= ind[1]
            row = ind[0]
            brow,bcol = Struct.get_2D_blk(row,col)
            #Collect unique values and counts for row col, squares
            unique_r,counts_r = np.unique(grid[row],return_counts=True)
            unique_c,counts_c = np.unique(grid[:,col],return_counts=True)
            unique_sq,counts_sq = np.unique(grid[brow,bcol].flat,return_counts=True)
            #All counts must be 1 with exception of 0 (first element)
            if (((counts_r[1:] == 1).all()) & ((counts_c[1:] == 1).all()) & ((counts_sq[1:] == 1).all())):
                continue
            else:
                return False
        else:
            continue
    return True
                
def start_sudoku(grid):
    """ A wrapper function to reset some data and
        Start the sudoku game
    """
    global backtrack,exec_time
    backtrack = 0
    exec_time = 0
    start_time = time.time()
    res = sudoku_solver(grid)
    exec_time =  time.time() - start_time
    if not res:
        print("Some error in the sudoku solver")
    
#This procedure solves the Sudoku one step at the time
def sudoku_solver(grid,i=0,j=0):
    global backtrack
    #find next empty cell to fill
    i,j = find_next_cell(grid)
    if i == -1: return True #The end
    #fill next cell
    for e in range(1,10):
        if is_valid(grid,i,j,e):
            grid[i,j] = e
            if sudoku_solver(grid,i,j):
                return True
            #failed attempt
            #undo current cell for back track
            backtrack += 1
            grid[i,j] = 0
    return False

def get_stats():
    return (backtrack,exec_time)
    



