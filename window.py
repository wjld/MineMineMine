from tkinter import Tk, ttk
from json import JSONDecodeError, load, dump

from draw import style


class Window:
    window = None
    size = None
    proportionalSize = None
    style = None
    menu = None
    game = None
    leaderboard = None
    leaderList = None
    savedGame = None
    minSquareSize = 40
    minTopRowY = 200
    minPad = 20
    sizes = {"Easy":(9,9,10),}

    def __init__(self):
        Window.window = Tk()
        Window.style = ttk.Style()
        self.window.title("Minesweeper")
        self.window.rowconfigure(0,weight=1)
        self.window.rowconfigure(1,weight=9)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        self.window.bind("<Configure>",self.manageSize)

        self.getLeaderboard()
        self.getSavedGame()
        Window.proportionalSize = self.getMinSize("Easy")
        self.setMinSize(*self.proportionalSize)

    def manageSize(self,event):
        if isinstance(event.widget,Tk) and self.isResizing(event):
            Window.size = (event.width,event.height)
            x,y = self.getMinSize("Easy")
            aspectRatio = x/y
            maxY = int(event.width/aspectRatio)

            if maxY < event.height:
                Window.proportionalSize = (event.width,maxY)
            else:
                Window.proportionalSize = self.size

            style(self.window,self.style,*self.proportionalSize)

    def isResizing(self,event):
        return (event.width,event.height) != self.size

    def getMinSize(self,level):
        x,y,_ = self.sizes[level]
        x = (x*self.minSquareSize)+(2*self.minPad)
        y = (y*self.minSquareSize)+(2*self.minPad)+self.minTopRowY
        return x,y

    def setMinSize(self,x,y):
        self.window.minsize(x,y)

    def setLeaderboard(self,leaderList):
        Window.leaderList = leaderList
        with open("./leaderboard.json","w") as leaderFile:
            dump(Window.leaderList,leaderFile)

    def getLeaderboard(self):
        try:
            with open("./leaderboard.json") as leaderFile:
                Window.leaderList = load(leaderFile)
        except(FileNotFoundError,JSONDecodeError):
            Window.leaderList = [["",0] for _ in range(10)]
            with open("./leaderboard.json","w") as leaderFile:
                dump(self.leaderList,leaderFile)

    def setSavedGame(self,savedGame):
        Window.savedGame = savedGame
        with open("./save.json","w") as saveFile:
                dump(Window.savedGame,saveFile)

    def getSavedGame(self):
        try:
            with open("./save.json") as saveFile:
                Window.savedGame = load(saveFile)
        except(FileNotFoundError,JSONDecodeError):
            Window.savedGame = {}
            with open("./save.json","w") as saveFile:
                dump(Window.savedGame,saveFile)

    def toMenu(self):
        self.getSavedGame()
        self.setMinSize(*self.getMinSize("Easy"))
        self.menu.display()

    def split(self,frame,xLength,yLength,xSize,ySize,i=0):
        if i < xLength or i < yLength:
            if i < xLength:
                frame.columnconfigure(i,minsize=xSize,weight=1)
            if i < yLength:
                frame.rowconfigure(i,minsize=ySize,weight=1)
            self.split(frame,xLength,yLength,xSize,ySize,i+1)