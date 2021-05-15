#tkinter docs
from tkinter import *
from tkinter import font
import random

top = Tk()

playlist = []
myRolls = []

myfont = font.Font(family='freemono', size=10, weight="bold")

def printList():
    print(playlist)

def exportPlaylist():
    with open('playlist.txt', 'w') as f:
        for song in playlist:
            f.write("%s/n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs", borderwidth=2, relief="ridge", font= myfont)
    LMain.grid(column = 1, row = 1)

    B1Main = Button(text = "Week 1", bg= "white",fg = "#4B0082", command = week1)
    B1Main.grid(column = 1, row = 3)

    B2Main = Button(text = "Week 2", bg = "white",fg = "#00008B", command = week2)
    B2Main.grid(column = 1, row = 4)

    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 1, row = 5)

def week1():

    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)
    
    clearWindow()
    #This is a Label widget
    L1 = Label(text= "Playlist Generator",fg = "#4B0082", borderwidth=2, relief="ridge", font= myfont)
    L1.grid(column= 0, row= 1)

    #This is a Text Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text= " + ", bg = "#9370DB", command = addSong)
    B1.grid(column = 1, row =2)

    B2 = Button(text= "Print List", bg = "#9370DB", command = printList)
    B2.grid(column = 4, row =2)

    B3 = Button(text= "Export List", bg = "#9370DB", command = exportPlaylist)
    B3.grid(column = 4, row =3)

    Bclear = Button(text="Main Menu", bg = "#9370DB", command= mainMenu)
    Bclear.grid(column = 0, row =40)

def week2():
    def rollDice():
        #access the entry data
        rollTimes = E2W2.get()
        dieType = E1W2.get()
        
        #clear the window
        clearWindow()
        
        #perform the dice roll calculations
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display the result with two labels and a button that goes to main menu
        L1RD = Label(top, text= "Here are your rolls!", fg = "#00008B", borderwidth=2,relief="ridge", font= myfont)
        L1RD.grid(column= 0, row= 1)

        L2RD = Label(top, borderwidth=2, relief="solid", bg = "#6495ED", text= "{}".format(myRolls))
        L2RD.grid(column= 0, row= 4)

        B1RD = Button(text= "Main Menu",bg = "#6495ED", command= mainMenu)
        B1RD.grid(column= 2, row= 8) 
                 
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App", fg = "#00008B", borderwidth=2,relief="ridge", font= myfont)
    L1W2.grid(column= 2, row= 1)
    
    L2W2 = Label(top, text= "# of Sides", fg = "#00008B")
    L2W2.grid(column= 1, row= 2)
    
    L3W2 = Label(top, text= "# of Rolls", fg = "#00008B")
    L3W2.grid(column= 3, row= 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column= 1, row= 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column= 3, row= 3)

    B1W2 = Button(text= "Roll 'em", bg = "#6495ED", command= rollDice)
    B1W2.grid(column= 2, row= 4) 
   

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

