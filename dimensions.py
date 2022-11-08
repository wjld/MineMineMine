def square(squareSize):
    nearStart = int((((squareSize) * 0.2)))
    nearEnd = squareSize - nearStart
    thickness = squareSize//15
    start = int(squareSize*0.1)
    end = squareSize - start
    middle = (squareSize)//2
    fontSize = int(-(squareSize*0.9))
    return [thickness,nearStart,nearEnd,start,end,middle,fontSize]

def mainFrame(x,y):
    return [20,50,x//20,y//50]

def statsFrame(minTopRowY,x):
    return [1,4,x//2,minTopRowY//4]

def optionsFrame(minTopRowY,x):
    return [5,20,x//10,minTopRowY//20]