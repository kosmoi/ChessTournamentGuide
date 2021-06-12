import tkinter as tk
from tkinter import Button, Label, Menu, ttk

import os

#create the Window
window = tk.Tk()
window.title("ChessTournamentGuide - CTG")
window.geometry("700x400")

#show all existing tournaments - function
tours = open("files/tournament_names.txt", "r")
tours2 = tours.read()

#functions:
def new_file():
    def new_tournament():
        input1 = oneEntry1.get()
        newtour = open("files/" + input1 + ".txt", "x")
        addtotxt = open("files/tournament_names.txt", "a")
        addtotxt.write(input1 + ", ")
        popup1.destroy()

    popup1 = tk.Toplevel()
    oneLabel1 = tk.Label(popup1, text="Enter the Name of the New tournament:")
    oneEntry1 = tk.Entry(popup1)
    oneButton1 = tk.Button(popup1, text="Create new tournament", command=new_tournament)

    oneLabel1.pack()
    oneEntry1.pack()
    oneButton1.pack()



def open_file():
    #elements of popup2
    popup2 = tk.Toplevel()
    twoLabel1 = tk.Label(popup2, text="Open one of following tournaments:")
    twoLabel2 = tk.Label(popup2, text=tours2)
    twoEntry1 = tk.Entry(popup2)
    twoButton1 = tk.Button(popup2, text="Open") #HIER GROSSE LÜCKE, mit drücken des buttons wird ein tunier geöffnet

    twoLabel1.pack()
    twoLabel2.pack()
    twoEntry1.pack()
    twoButton1.pack()



def delete_file():


    popup3 = tk.Toplevel()
    threeLabel1 = tk.Label(popup3, text="Delete one of following tournaments:")
    threeLabel2 = tk.Label(popup3, text=tours2)
    threeEntry1 = tk.Entry(popup3)

    def delete_tournament():
        input2 = threeEntry1.get()
        os.remove("files/" + input2 + ".txt")
        popup3.destroy()

    threeButton1 = tk.Button(popup3, text="Delete", command=delete_tournament)

    threeLabel1.pack()
    threeLabel2.pack()
    threeEntry1.pack()
    threeButton1.pack()



#create the menubar
menubar = tk.Menu(window, font=20)

#creae single elements of the menubar
menu_file = tk.Menu(menubar)
menu_file.add_command(label="New", command=new_file)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Delete", command=delete_file)
menu_file.add_command(label="------")
menu_file.add_command(label="Close Program", command=window.quit)
menu_tour = tk.Menu(menubar)
menu_tour.add_command(label="New Round")
menu_tour.add_command(label="Enter Results")
menu_player = tk.Menu(menubar)
menu_player.add_command(label="Add Player")
menu_about = tk.Menu(menubar)
menu_about.add_command(label="Contributer")
menu_about.add_command(label="README.txt")

menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Tournament", menu=menu_tour)
menubar.add_cascade(label="Player", menu=menu_player)
menubar.add_cascade(label="About", menu=menu_about)
window.config(menu=menubar)


window.mainloop()