from tkinter import Canvas, ttk
from random import randint

from window import Window


class Game(Window):
    def __init__(self,_continue=False):
        self.labelFrame = ttk.Frame(self.window)
        self.optionsFrame = ttk.Frame(self.window)
        self.gameFrame = ttk.Frame(self.window,)
        self.squares:dict[tuple,Canvas] = {}

        self.labelFrame.grid(row=0,column=0,sticky="nsew")
        self.optionsFrame.grid(row=0,column=1,sticky="nsew")
        self.gameFrame.grid(row=1,columnspan=2,padx=20,pady=20,sticky="nsew")
        self.split(self.labelFrame,1,1,200,200,1,1)
        self.split(self.optionsFrame,5,20,40,10,1,1)

        self.started = False
        self.xLength,self.yLength = 9,9
        self.minesQ = 10
        self.opened = 0
        self.split(self.gameFrame,self.xLength,self.yLength,40,40,1,1)
        self.setWidgets(_continue)

    def setWidgets(self,_continue):
        title = ttk.Label(self.labelFrame,text="000",style="time.TLabel")
        saveB = ttk.Button(self.optionsFrame,command=self.save,text="Save",style="smallOptions.TButton")
        quitB = ttk.Button(self.optionsFrame,command=self.quit,text="Quit",style="smallOptions.TButton")

        title.grid()
        saveB.grid(row=6,column=1,rowspan=4,columnspan=3,sticky="nsew")
        quitB.grid(row=10,column=1,rowspan=4,columnspan=3,sticky="nsew")

        if not _continue:
            self.generateField(0,0)
        self.drawField(list(self.savedGame.items()))

    def generateField(self,r:int,c:int,recursion=False):
        opened,flagged,mined,count = False,False,False,0
        self.savedGame[f"{r} {c}"] = [opened,flagged,mined,count]

        if r < self.yLength - 1 and not recursion:
            self.generateField(r+1,c)
        if c < self.xLength - 1:
            self.generateField(r,c+1,True)

    def drawField(self,field):
        if field:
            info = field.pop()
            r,c = map(int,info[0].split())
            opened,flagged,mined,count = info[1]
            if not opened:
                color = "gray40" if (r+c)%2 else "gray45"
            else:
                color = "gray70" if (r+c)%2 else "gray80"
            square = Canvas(self.gameFrame,width=10,height=10,bg=color,highlightthickness=0)
            square.grid(row=r,column=c,sticky="nsew")
            self.squares[(r,c)] = square

            if opened or flagged:
                self.write(r,c)

            square.bind("<1>",lambda e,r=r,c=c,:self.open(r,c))
            square.bind("<3>",lambda e,r=r,c=c:self.flag(r,c))
            square.bind("<Enter>",lambda e,r=r,c=c:self.hover(r,c,True))
            square.bind("<Leave>",lambda e,r=r,c=c:self.hover(r,c,False))

            self.drawField(field)

    def hover(self,row,column,hovering):
        square = self.squares[(row,column)]
        opened,*_ = self.savedGame[f"{row} {column}"]
        if not opened and hovering:
            square.config(bg="gray95")
        elif not opened:
            color = "gray40" if (row+column)%2 else "gray45"
            square.config(bg=color)

    def open(self,row,column):
        self.savedGame[f"{row} {column}"][0] = True
        square = self.squares[(row,column)]
        color = "gray70" if (row+column)%2 else "gray80"
        square.config(bg=color)

    def iterAdjacent(self):
        pass

    def inField(self,row,column):
        pass

    def flag(self,row,column):
        pass

    def layMines(self,quantity,row,column):
        pass

    def count(self):
        pass

    def write(self,row,column):
        pass

    def win(self):
        pass

    def lose(self,square):
        self.quit()

    def save(self):
        self.setSavedGame()
        self.quit()

    def quit(self):
        self.labelFrame.destroy()
        self.gameFrame.destroy()
        self.optionsFrame.destroy()