"""
This is a personal project in which I created a Tic Toc Toe game using Python's Tkinter Library
I have been inspired by Codemy.com and the video: https://www.youtube.com/watch?v=xx0qmpuA-vM
@author: Bertan Berker
@Language: Python 3.9
"""

from tkinter import *
from tkinter import messagebox


# Initializing the GUI window
window = Tk()

window.title('Tic Tac Toe')

# True means X's turn
clicked = True
count = 0

"""
This function disable all the buttons
:parameter: No parameters
:return: Void
"""

def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


"""
This function checks if the game is over, whether it is won by X, O or it is a tie
:parameter: No parameters
:return: Void
"""

def checkIfWon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()


    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()


    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()


    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()


    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins!")
        disable_all_buttons()


    # Check for O's

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()


    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()


    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()


    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()


    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations O wins!")
        disable_all_buttons()


    # Check if it is a tie

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", " It's a Tie!\nNo one wins")
        disable_all_buttons()


"""
This function changes the text on the button (writes X or O if empty)
:parameter button: The button that has been clicked
:return: Void
"""

def click(button):
    global clicked, count

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkIfWon()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box")


"""
This function starts the game from the beginning and creates and puts the buttons on the grid
:parameter: No parameters
:return: Void
"""

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    #Building buttons
    b1 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b1))
    b2 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b2))
    b3 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b3))
    b4 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b4))
    b5 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b5))
    b6 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b6))
    b7 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b7))
    b8 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b8))
    b9 = Button(window, text = " ", font=("Times New Roman", 20), height = 3, width = 6, command = lambda: click(b9))

    # Grid the buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Create menu for having the choice to restart the game

my_menu = Menu(window)
window.config(menu = my_menu)

# Create options menu

options_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Rest Game", command = reset)

reset()
window.mainloop()