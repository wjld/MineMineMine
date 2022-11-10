from tkinter import ttk

from window import Window
from dimensions import mainFrame


class Leaderboard(Window):
    def __init__(self):
        Window.leaderboard = self
        self.frame = ttk.Frame(self.window)
        self.scores = []

        self.frame.grid(row=0,column=0,rowspan=2,columnspan=2,sticky="nsew")
        self.split(self.frame,*mainFrame(*self.getMinSize("Easy")))
        self.getLeaderboard()
        self.setWidgets()
        self.frame.grid_remove()

    def display(self):
        self.frame.grid()
        self.getLeaderboard()
        self.displayBoard()

    def setWidgets(self):
        title = ttk.Label(self.frame,text="HIGHSCORES",style="title.TLabel")
        resetB = ttk.Button(self.frame,command=self.reset,
                            text="Reset",style="options.TButton",width=5)
        backB = ttk.Button(self.frame,command=self.back,
                           text="Back",style="options.TButton",width=4)
        title.grid(row=1,column=1,rowspan=5,columnspan=18)
        resetB.grid(row=6,column=1,rowspan=4,columnspan=6,sticky="nsew")
        backB.grid(row=6,column=13,rowspan=4,columnspan=6,sticky="nsew")
        self.setBoard()

    def setBoard(self,scores=None,x=None):
        if scores is None:
            x = 10
            scores = list(enumerate(self.leaderList,1))[::-1]
        if scores:
            order,data = scores.pop()
            score = f"{order:02d} - {data[0]:^11} - {data[1]:03d}"
            score = ttk.Label(self.frame,text=score,style="highscore.TLabel")
            self.scores.append(score)
            score.grid(row=x,column=1,rowspan=4,columnspan=18)
            self.setBoard(scores,x+4)

    def displayBoard(self,scores=None):
        if scores is None:
            scores = list(enumerate(self.leaderList,1))[::-1]
        if scores:
            order,data = scores.pop()
            score = f"{order:02} - {data[0]:^11} - {data[1]:03}"
            self.scores[order-1].configure(text=score)
            self.displayBoard(scores)

    def reset(self):
        self.setLeaderboard([["",0] for _ in range(10)])
        self.displayBoard()

    def back(self):
        self.frame.grid_remove()
        self.toMenu()