from tkinter import ttk

from window import Window
from game import Game
from leaderboard import Leaderboard
from dimensions import mainFrame


class Menu(Window):
    def __init__(self):
        self.saved = bool(self.savedGame)
        self.frame = ttk.Frame(self.window)

        self.frame.grid(rowspan=2,columnspan=2,sticky="nsew")
        self.split(self.frame,*mainFrame(400,600))
        self.setWidgets()

    def setWidgets(self):
        title = ttk.Label(self.frame,text="MINESWEEPER",style="title.TLabel")
        newGameB = ttk.Button(self.frame,command=self.newGame,
                              text="New Game",style="options.TButton")
        continueB = ttk.Button(self.frame,command=self._continue,
                               text="Continue Game",style="options.TButton")
        leaderboardB = ttk.Button(self.frame,command=self.leaderboard,
                                  text="Leaderboard",style="options.TButton")
        quitB = ttk.Button(self.frame,command=self.quit,text="Quit",
                           style="options.TButton")

        title.grid(row=2,column=1,rowspan=5,columnspan=18)
        newGameB.grid(row=25,column=5,rowspan=4,columnspan=10,sticky="nsew")
        continueB.grid(row=30,column=5,rowspan=4,columnspan=10,sticky="nsew")
        leaderboardB.grid(row=35,column=5,rowspan=4,columnspan=10,
                          sticky="nsew")
        quitB.grid(row=40,column=5,rowspan=4,columnspan=10,sticky="nsew")

        if not self.saved:
            continueB.state(["disabled"])

    def newGame(self):
        Game()

    def _continue(self):
        Game(_continue=True)

    def leaderboard(self):
        Leaderboard()

    def quit(self):
        self.window.destroy()