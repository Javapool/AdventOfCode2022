from functools import reduce
from posixpath import split
from turtle import shapesize

import mysqlx
import utilities

resultDict = {
    'Rock':{
        'Win':'Paper',
        'Draw':'Rock',
        'Lose':'Scissors',
        },
    'Paper':{
        'Win':'Scissors',
        'Draw':'Paper',
        'Lose':'Rock',
        },
    'Scissors':{
        'Win':'Rock',
        'Draw':'Scissors',
        'Lose':'Paper',
        },
}

enemyShapes = {
    'A':'Rock',
    'B':'Paper',
    'C':'Scissors'
}

myShapes = {
    'X':'Rock',
    'Y':'Paper',
    'Z':'Scissors'
}

shapeScore = {
    'Rock':1,
    'Paper':2,
    'Scissors':3
}

plannedResult = {
    'X':'Lose',
    'Y':'Draw',
    'Z':'Win'
}

gamescore = {
    -1:0,
    0:3,
    1:6
}

def compareShapes(opponent, player):
    if opponent == player:
        return 0
    if opponent == 'Rock':
        if player == 'Scissors':
            return -1
        else:
            return 1
    if opponent == 'Scissors':
        if player == 'Paper':
            return -1
        else:
            return 1
    if opponent == 'Paper':
        if player == 'Rock':
            return -1
        else:
            return 1

def calcScore(shapes):
    oppShape = enemyShapes[shapes[0]]
    myShape = myShapes[shapes[1]]
    #print(myShape,' Vs. ',oppShape)
    return gamescore[compareShapes(oppShape,myShape)]+shapeScore[myShape]
    #return gamescore[compareShapes(shapes[0], shapes[1])]+shapeScore[myShapes[shapes[1]]]

def calcScore2(shapes):
    oppShape = enemyShapes[shapes[0]]
    myShape = resultDict[oppShape][plannedResult[shapes[1]]]
    return gamescore[compareShapes(oppShape,myShape)]+shapeScore[myShape]

def main():
    file = utilities.readFile("C:\Repos\AdventOfCode2022\Day-2\input2.txt")
    lines = file.splitlines()
    splitLines = list(map(lambda x: x.split(' '),lines))
    #print(splitLines)
    print(reduce(lambda x,y: x+ calcScore2(y),splitLines,0))
    #print(part1())
    #print(part2())

def part1():
    pass

def part2():
    pass


if __name__== "__main__" :
    main()