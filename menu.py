from tkinter import Tk, ttk

class Menu:
    def __init__(self,window:Tk,leaderboard:list,savedGame:dict):
        self.window = window
        self.leaderList = leaderboard
        self.savedDict = savedGame
        self.saved = savedGame["board"] is not None
        self.frame = ttk.Frame(self.window)

        ttk.Style().configure("title.TLabel", font=("Courier New",40))
        ttk.Style().configure("options.TButton", font=("Courier New",15))

        self.window.minsize(400, 600)
        self.window.columnconfigure(0,weight=1)
        self.window.rowconfigure(0,weight=1)

        self.frame.grid(sticky='nsew')
        self.split()
        self.setWidgets()
    
    def split(self):
        for i in range(60):
            if i < 20:
                self.frame.columnconfigure(i,minsize=20,weight=1)
            self.frame.rowconfigure(i,minsize=10,weight=1)       

    def setWidgets(self):
        title = ttk.Label(self.frame,text="MINESWEEPER",style="title.TLabel")
        newGameB = ttk.Button(self.frame,command=self.newGame,text="New Game",style="options.TButton")
        _continueB = ttk.Button(self.frame,command=self._continue,text="Continue Game",style="options.TButton")
        leaderboardB = ttk.Button(self.frame,command=self.leaderboard,text="Leaderboard",style="options.TButton")
        quitB = ttk.Button(self.frame,command=self.quit,text="Quit",style="options.TButton")

        title.grid(row=8,column=1,rowspan=6,columnspan=18)
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
        pass

    def quit(self):
        self.window.destroy()