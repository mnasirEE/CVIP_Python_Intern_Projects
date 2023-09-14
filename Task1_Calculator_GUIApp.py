"""
Created on Sun Aug 20 00:17:47 2023

@author: M.Nasir

"""
""" Phase1: Normal Task
        1. Calculator
        The objective of this project is to design and develop a calculator application in Python that
        allows users to perform basic arithmetic operations such as addition, subtraction,
        multiplication, and division. The application should provide a user-friendly interface and
        accurate calculations. 
"""
# Calculator Using Tkinter

import tkinter as tk
root = tk.Tk()
root.title("Nasir's Calculator")
root.geometry("585x395")

# Entry of values to calculate and displays result after calculation
value = tk.Entry(root, width= 20 , font= "serif 40")
value.grid(row=0,column=0, columnspan= 4)

# function called what an event occurs means when buttons are clicked
def click_button(event):
    current = value.get()
    text = event.widget.cget("text")
    if text == '=':
        result = eval(current)
        value.delete(0, tk.END)
        value.insert(tk.END, str(result))
    elif text == 'C':
        value.delete(0, tk.END)

    else:
        value.insert(tk.END, text)

# Buttons names
buttons = [
    '9', '8', '7', '/',
    '6', '5', '4', '*',
    '3', '2', '1', '-',
    '0', '.', '=', '+',
    'C'
    ]

# add Buttons on screen
rows = 1
cols = 0
for i in buttons:
  
    a = tk.Button(root, text= i, font= "serif 15 bold", width= 11, height= 2)
    a.grid(row= rows, column= cols)
    a.bind("<Button-1>", click_button )
    cols = cols + 1
    if cols == 4:
        cols = 0
        rows = rows + 1

root.mainloop()