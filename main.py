from tkinter import Tk
from window import Window
from menu import Menu
from json import load, dump

if __name__ == "__main__":
    try:
        with open("./leaderboard.json") as leaderFile:
            leaderboard = load(leaderFile)
    except(FileNotFoundError):
        leaderboard = [[x,""] for x in range(1,11)]
        with open("./leaderboard.json","x") as leaderFile:
            dump(leaderboard,leaderFile)
    try:
        with open("./save.json") as saveFile:
            savedGame = load(saveFile)
    except(FileNotFoundError):
        savedGame = {"board":None,"mines":None}
        with open("./save.json","x") as saveFile:
            dump(savedGame, saveFile)

    window = Tk()
    window.title("Minesweeper")
    Window(window)
    Menu(window,leaderboard,savedGame)
    window.mainloop()