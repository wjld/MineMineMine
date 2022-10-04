from tkinter import Tk, ttk

class Window:
    window = Tk()
    
    def __init__(self):
        self.window.title("Minesweeper")
        self.window.minsize(400, 600)
        self.window.columnconfigure(0,weight=1)
        self.window.rowconfigure(0,weight=1)

        ttk.Style().configure("title.TLabel", font=("Courier New",40))
        ttk.Style().configure("description.TLabel", font=("Courier New",20))
        ttk.Style().configure("options.TButton", font=("Courier New",15))
    
    def split(self,frame:ttk.Frame,xLength:int,yLength:int,xSize:int,ySize:int,xWeight:int,yWeight:int):
        for i in range(max(xLength,yLength)):
            if i < xLength:
                frame.columnconfigure(i,minsize=xSize,weight=xWeight)
            if i < yLength:
                frame.rowconfigure(i,minsize=ySize,weight=yWeight)