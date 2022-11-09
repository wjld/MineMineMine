from tkinter import Canvas, ttk
from random import randint

from window import Window
import dimensions


class Game(Window):
    def __init__(self,_continue=False):
        Window.game = self
        self.started = False
        self.opened = 0
        self.statsFrame = ttk.Frame(self.window)
        self.optionsFrame = ttk.Frame(self.window)
        self.gameFrame = ttk.Frame(self.window,)
        self.squares:dict[tuple,Canvas] = {}
        self.xLength,self.yLength,self.minesQ = self.sizes["Easy"]

        self.statsFrame.grid(row=0,column=0,sticky="nse")
        self.optionsFrame.grid(row=0,column=1,sticky="nsw")
        self.gameFrame.grid(row=1,columnspan=2,padx=self.minPad,
                            pady=self.minPad,sticky="nsew")
        self.split(self.statsFrame,*dimensions.statsFrame(self.minTopRowY,
                   self.getMinSize("Easy")[0]))
        self.split(self.optionsFrame,*dimensions.optionsFrame(self.minTopRowY,
                   self.getMinSize("Easy")[0]))
        self.split(self.gameFrame,self.xLength,self.yLength,
                   self.minSquareSize,self.minSquareSize)

        self.setWidgets(_continue)

    def setWidgets(self,_continue):
        timer = ttk.Label(self.statsFrame,text="000",style="stats.TLabel")
        mines = ttk.Label(self.statsFrame,text="000",style="stats.TLabel")
        saveB = ttk.Button(self.optionsFrame,command=self.save,text="Save",
                           style="smallOptions.TButton",width=4)
        quitB = ttk.Button(self.optionsFrame,command=self.quit,text="Quit",
                           style="smallOptions.TButton",width=4)

        timer.grid(row=0,rowspan=2,sticky="nsew")
        mines.grid(row=2,rowspan=2,sticky="nsew")
        saveB.grid(row=1,column=1,rowspan=5,columnspan=3,sticky="nsew")
        quitB.grid(row=7,column=1,rowspan=5,columnspan=3,sticky="nsew")

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
        self.statsFrame.destroy()
        self.gameFrame.destroy()
        self.optionsFrame.destroy()
        self.toMenu()