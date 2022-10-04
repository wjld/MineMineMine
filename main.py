from tkinter import Tk
from window import Window
from menu import Menu
from json import JSONDecodeError, load, dump

if __name__ == "__main__":
    try:
        with open("./leaderboard.json") as leaderFile:
            leaderboard = load(leaderFile)
    except(FileNotFoundError, JSONDecodeError):
        leaderboard = [["",0] for _ in range(10)]
        with open("./leaderboard.json","w") as leaderFile:
            dump(leaderboard,leaderFile)
    try:
        with open("./save.json") as saveFile:
            savedGame = load(saveFile)
    except(FileNotFoundError, JSONDecodeError):
        savedGame = {"board":None,"mines":None}
        with open("./save.json","w") as saveFile:
            dump(savedGame, saveFile)

    Window()
    Menu(leaderboard,savedGame)
    Window.window.mainloop()