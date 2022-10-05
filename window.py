from tkinter import Tk, ttk
from json import JSONDecodeError, load, dump

class Window:
    window = Tk()
    window.title("Minesweeper")
    window.minsize(400, 600)
    window.columnconfigure(0,weight=1)
    window.rowconfigure(0,weight=1)
    leaderList = []
    savedGame = {}
    
    def __init__(self):
        ttk.Style().configure("title.TLabel", font=("Courier New",40))
        ttk.Style().configure("description.TLabel", font=("Courier New",20))
        ttk.Style().configure("options.TButton", font=("Courier New",15))

        self.getLeaderboard()
        self.getSavedGame()
    
    def setLeaderboard(self):
        Window.leaderList = [["",0] for _ in range(10)]
        with open("./leaderboard.json","w") as leaderFile:
            dump(Window.leaderList,leaderFile)
    
    def getLeaderboard(self):
        try:
            with open("./leaderboard.json") as leaderFile:
                Window.leaderList = load(leaderFile)
        except(FileNotFoundError, JSONDecodeError):
            Window.leaderList = [["",0] for _ in range(10)]
            with open("./leaderboard.json","w") as leaderFile:
                dump(self.leaderList,leaderFile)
    
    def getSavedGame(self):
        try:
            with open("./save.json") as saveFile:
                Window.savedGame = load(saveFile)
        except(FileNotFoundError, JSONDecodeError):
            Window.savedGame = {"board":None,"mines":None}
            with open("./save.json","w") as saveFile:
                dump(Window.savedGame, saveFile)
    
    def split(self,frame:ttk.Frame,xLength:int,yLength:int,xSize:int,ySize:int,xWeight:int,yWeight:int):
        for i in range(max(xLength,yLength)):
            if i < xLength:
                frame.columnconfigure(i,minsize=xSize,weight=xWeight)
            if i < yLength:
                frame.rowconfigure(i,minsize=ySize,weight=yWeight)