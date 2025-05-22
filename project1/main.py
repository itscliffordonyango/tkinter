# This is the first project of my 15 python projects before 10th June 2025

# Simple tkinter app to display a welcome message to the user 

import tkinter as tk
from tkinter import *



mainwindow =tk.Tk()
mainwindow.title("Chax App")
mainwindow.geometry("1000x650")
mainwindow.config(bg="#000b6b")
mainwindow.resizable(True,True) #allow user to reize the window 

# second window to explore 
def explore_window():
    explore_window = tk.Toplevel(mainwindow)
    explore_window.title("Explore")
    explore_window.geometry("800x600")
    explore_window.config(bg="#000b6b")
    explore_window.resizable(True,True) #allow user to reize the window 
    
    content = Label(
        explore_window,
        text="This is the \n explore window",
        fg="#69f5ff",
        bg="#000b6b",
        font=("Arial", 20, "bold"),
        anchor="center",
        width=20,
        height=4,
        border=4,
    )
    content.pack(pady=(20, 2))
    
    close=Button(
        explore_window,
        text ="Exit",
        fg="#000f09",
        bg="#b5040c",
        font=("Arial", 20, "bold"),
        border=4,
        activebackground="#b5040c",
        activeforeground="#000f09",
        command= lambda: explore_window.destroy(),
        anchor="se",
        relief="raised",        
    )
    close.pack(side="right", padx=20)
        
    explore_window.mainloop()

# lets put the labels that will hold the cool stuffs 

# put them in a function 
def welcome():
    Welcome = Label(
    mainwindow,
    text="Welcome dear user \n to my amazing app",
    fg="#69f5ff",
    bg="#000b6b",
    font=("Arial", 30, "bold"),
    anchor="center",
    width=20,
    height=4,
    border=4,
)
    Welcome.pack(pady=(20, 2)) # add some padding to the top of the label

def options():
    options = Label(
        mainwindow,
        text=" Choose an action \n to perform",
        fg="#69f5ff",
        bg= "#000b6b",
        font=("Arial", 20, "bold"),
        anchor="center",
        width=20,
        height=4,
        border=4,
    )
    
    options.pack(pady=(0,40))


def explore():
    explore= Button(
        mainwindow,
        text= "Explore",
        fg="#13f22a",
        bg="#d1f213",
        height="1",
        width="7",
        font=("Arial", 20, "bold"),
        border=4,
        activebackground="#d1f213",
        activeforeground="#13f22a",
        command= lambda: explore_window(),
        anchor="sw",
        relief="raised",        
    )
    explore.pack(side="left", padx=20)
    # explore.place(x=100, y=200)
    # explore.place(x=100, y=200)

def exit():
    exit=Button(
        mainwindow,
        text ="Exit",
        fg="#000f09",
        bg="#b5040c",
        font=("Arial", 20, "bold"),
        border=4,
        activebackground="#b5040c",
        activeforeground="#000f09",
        command= lambda: mainwindow.destroy(),
        anchor="se",
        relief="raised",
        
    )
    exit.pack(side="right", padx=20)
    
# call the functions
welcome()
options()
explore()
exit()
mainwindow.mainloop()