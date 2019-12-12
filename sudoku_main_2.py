# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:00:00 2019

@author: Andre
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from output import gen_output
from sudokuRecursive import start_sudoku,sudoku_validate,get_stats
from datetime import datetime

sudoku = np.zeros((9,9),dtype=np.int16)



def check_digit(char):
    """
    Check that the char is a digit between 1-9
    Input is a string (char)
    Return True if between 1-9
    False otherwise
    """
    if char.isdigit():
        if (int(char) > 0) & (int(char) < 10):
            return True
    return False  


def start():
    """
    Read data from the Entries.
    Perform some basic validation.
    Start the Sudoku game
    """
    global sudoku
    sudoku.fill(0)
    
    #scan all entries and collect data
    init = [] #list with the coordinates for the initial values
    for k,v in ent_dict.items():
        txt = v.get()
        if txt:
            if check_digit(txt):
                sudoku[k[0],k[1]]=int(txt)
                init.append((k[0],k[1]))
            else:
                #Wrong input
                v.config({"background": "Red"})
                print("Error, all inputs must be between 1-9")
                print("Invalid input is: ",txt," in position: ",k)
                txt_var0 = "Error, all inputs must be between 1-9\n"+"Press Clear\n"+"Enter new data"
                txt_res.insert(tk.INSERT,txt_var0)
                return False
    #All initial data collected
    #Set the Start button to disabled
    st.config(state=tk.DISABLED)
    #start the game
    if  sudoku_validate(sudoku):
        start_sudoku(sudoku)
        gen_output(fr_result,sudoku,set(init))
        time_stamp = "Game at "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n" 
        txt_res.insert(tk.INSERT,time_stamp)
        backtrack,exec_time = get_stats()
        txt_var1 = "the number of recursion steps are:  " + str(backtrack) + "\n" 
        txt_res.insert(tk.INSERT,txt_var1)
        exec_time = round(exec_time,2)
        if exec_time < 0.5:
            exec_time = " less than 0.5 seconds "
        txt_var2 = "the approximated execution time in seconds :  " + str(exec_time) + "\n" + "\n" 
        txt_res.insert(tk.INSERT,txt_var2)
        
    else:
        print(">>>>>>>>Invalid initial data>>>>>>>>>")
        txt_var3 = "Invalid Initial data configuration.\nPress Clear "+ "\n"+ "Enter new correct configuration"
        txt_res.insert(tk.INSERT,txt_var3)

    
def clear_input():
    """
    Clear the input matrix 
    Clear the the input FRame
    """
    global sudoku
    sudoku.fill(0)
    st.config(state=tk.NORMAL)
    #Clear the input frame
    for k,v in ent_dict.items():
        if v.get():
            v.config({"background": "White"})
            v.delete(0,'end')



#Table  convert frame position into matrix 
offset_table={0:(0,0),1:(0,3),2:(0,6),
         3:(3,0),4:(3,3),5:(3,6),
         6:(6,0),7:(6,3),8:(6,6)}

window = tk.Tk()
window.title('Sudoku')
window.geometry("1200x900")
###The window is structured into four main frames:
#1-Main text
fr_title = tk.Frame(window,width=100, height=100)
label_title = tk.Label(fr_title,text="My Sudoku solver",font=("Courier", 30,"bold"))
fr_title.grid(row=0)
label_title.grid(row=0,columnspan=4,ipadx=100)
#2-Sudoku initial configuration  and control buttoms
fr_init = tk.Frame(window,width=500, height=500, bd= 1,highlightbackground="green")
fr_init.grid(row=2,column=0,ipady=80)
tk.Label(fr_init,text="Initial data",font="helvetica 15").grid(row=0,columnspan=3)
#3-Game result
fr_result = tk.Frame(window,width=300, height=300, bd= 1,highlightbackground="red")
fr_result.grid(row=2,column=1,ipady=80)
#4-Some info txt about result
fr_txt = tk.Frame(window,width =300,height =100,highlightcolor="blue", highlightthickness=1)
fr_txt.grid(row=3,column=0)

########Configure the "Initial Frame"
#A Sudoku matrix (9x9) for initial data is placed in the initial FRame.
#The matrix divided into 9 sub matrices (3x3). 
#Each sub matrix is an own frame with 9 Entries
#The user enters the initial data in the corresponding Entries
frame_l = [] #list with the frames for the sub matrices
ent_dict = {}
#Create the 9  frames, one for each 3X3 sub matrix 
for cr in ((1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)):
    frame_in=tk.Frame(fr_init, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    frame_in.grid(row=cr[0],column=cr[1])
    frame_l.append(frame_in)
#Configure all the entries
#Each Entry is placed in a corresponding sub matrix (3X3)
for ind,f in enumerate(frame_l):
    for cr in ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)):
        ent1 = ttk.Entry(master=f,width=3)
        ent1.grid(row=cr[0],column=cr[1])
        ##transform GUI position to matrix indices
        ##Store corresponding matrix indices,Entry
        offset=offset_table[ind]
        ent_dict[(offset[0]+cr[0],offset[1]+cr[1])] = ent1
        

# #Start Buttom command
st = ttk.Button(fr_init,text = "Start  ",command=start)
st.grid(row=5,column=0,columnspan=2,sticky='w')
 #Clear
ct = ttk.Button(fr_init,text = "Clear ",command=clear_input)
ct.grid(row=5,column=2,columnspan=2)

#########Configure the FRame with the text
#Txt with info about result 
txt_res = tk.Text(master=fr_txt,width = 60 ,height = 10,font="Helvetica 10")
txt_res.grid(column=0,row=0)




window.mainloop()
