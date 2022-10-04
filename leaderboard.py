from tkinter import ttk
from window import Window
from json import dump

class Leaderboard(Window):
    def __init__(self,leaderList:list[list]):
        self.leaderList = leaderList
        self.frame = ttk.Frame(self.window)
        
        self.frame.grid(row=0,column=0,sticky='nsew')
        self.split(self.frame,20,60,20,10,1,1)
        self.setWidgets()
    
    def setWidgets(self):
        title = ttk.Label(self.frame,text="HIGHSCORES",style="title.TLabel")
        resetB = ttk.Button(self.frame,command=self.reset,text="Reset",style="options.TButton")
        backB = ttk.Button(self.frame,command=self.back,text="Back",style="options.TButton")
        scores = []
        for order, data in enumerate(self.leaderList, 1):
            score = f"{order:02d} - {data[0]:^8} - {data[1]:03d}"
            scores.append(ttk.Label(self.frame,text=score,style="description.TLabel"))

        title.grid(row=1,column=1,rowspan=7,columnspan=18)
        x = 19
        for score in scores:
            score.grid(row=x,column=1,rowspan=4,columnspan=18)
            x += 4
        resetB.grid(row=9,column=1,rowspan=4,columnspan=8,sticky='nsew')
        backB.grid(row=9,column=11,rowspan=4,columnspan=8,sticky='nsew')
    
    def reset(self):
        self.leaderList = [["",0] for _ in range(10)]
        with open("./leaderboard.json","w") as leaderFile:
            dump(self.leaderList,leaderFile)
        
        self.frame.destroy()
        self.frame = ttk.Frame(self.window)
        self.frame.grid(row=0,column=0,sticky='nsew')
        self.split(self.frame,20,60,20,10,1,1)
        self.setWidgets()

    def back(self):
        self.frame.destroy()