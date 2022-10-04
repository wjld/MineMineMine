from tkinter import ttk
from window import Window
from game import Game
from leaderboard import Leaderboard
from json import JSONDecodeError, load, dump

class Menu(Window):
    def __init__(self):
        try:
            with open("./save.json") as saveFile:
                self.savedGame = load(saveFile)
        except(FileNotFoundError, JSONDecodeError):
            self.savedGame = {"board":None,"mines":None}
            with open("./save.json","w") as saveFile:
                dump(self.savedGame, saveFile)

        self.saved = self.savedGame["board"] is not None
        self.frame = ttk.Frame(self.window)

        self.frame.grid(sticky='nsew')
        self.split(self.frame,20,60,20,10,1,1)
        self.setWidgets()    

    def setWidgets(self):
        title = ttk.Label(self.frame,text="MINESWEEPER",style="title.TLabel")
        newGameB = ttk.Button(self.frame,command=self.newGame,text="New Game",style="options.TButton")
        _continueB = ttk.Button(self.frame,command=self._continue,text="Continue Game",style="options.TButton")
        leaderboardB = ttk.Button(self.frame,command=self.leaderboard,text="Leaderboard",style="options.TButton")
        quitB = ttk.Button(self.frame,command=self.quit,text="Quit",style="options.TButton")

        title.grid(row=6,column=1,rowspan=7,columnspan=18)
        newGameB.grid(row=30,column=5,rowspan=4,columnspan=10,sticky='nsew')
        _continueB.grid(row=35,column=5,rowspan=4,columnspan=10,sticky='nsew')
        leaderboardB.grid(row=40,column=5,rowspan=4,columnspan=10,sticky='nsew')
        quitB.grid(row=45,column=5,rowspan=4,columnspan=10,sticky='nsew')

        if not self.saved:
            _continueB.state(['disabled'])

    def newGame(self):
        pass

    def _continue(self):
        pass

    def leaderboard(self):
        try:
            with open("./leaderboard.json") as leaderFile:
                leaderList = load(leaderFile)
        except(FileNotFoundError, JSONDecodeError):
            leaderList = [["",0] for _ in range(10)]
            with open("./leaderboard.json","w") as leaderFile:
                dump(leaderList,leaderFile)
        Leaderboard(leaderList)

    def quit(self):
        self.window.destroy()