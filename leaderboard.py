from tkinter import ttk

from window import Window
from dimensions import mainFrame


class Leaderboard(Window):
    def __init__(self):
        self.frame = ttk.Frame(self.window)

        self.frame.grid(row=0,column=0,rowspan=2,columnspan=2,sticky="nsew")
        self.split(self.frame,*mainFrame(400,600))
        self.getLeaderboard()
        self.setWidgets()

    def setWidgets(self):
        title = ttk.Label(self.frame,text="HIGHSCORES",style="title.TLabel")
        resetB = ttk.Button(self.frame,command=self.reset,
                            text="Reset",style="options.TButton",width=5)
        backB = ttk.Button(self.frame,command=self.back,
                           text="Back",style="options.TButton",width=4)
        scores = []
        for order, data in enumerate(self.leaderList, 1):
            score = f"{order:02d} - {data[0]:^8} - {data[1]:03d}"
            scores.append(ttk.Label(self.frame,text=score,style="highscore.TLabel"))

        title.grid(row=1,column=1,rowspan=5,columnspan=18)
        x = 10
        for score in scores:
            score.grid(row=x,column=1,rowspan=4,columnspan=18)
            x += 4
        resetB.grid(row=6,column=1,rowspan=4,columnspan=6,sticky="nsew")
        backB.grid(row=6,column=13,rowspan=4,columnspan=6,sticky="nsew")

    def reset(self):
        self.setLeaderboard()
        self.getLeaderboard()

        for widget in self.frame.winfo_children():
            widget.destroy()
        self.setWidgets()

    def back(self):
        self.frame.destroy()