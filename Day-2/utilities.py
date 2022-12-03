from contextlib import nullcontext


def readFile(filename):
    file = open(filename,'r')
    return file.read()

def findMax(list):
    currentMax = 'null'
    for number in list:
        if currentMax == 'null' or number > currentMax:
            currentMax = number
    return currentMax

def findMaxNResults(list, n):
    maxCandidates = []
    numberInList = 0
    inserted = False
    for number in list:
        inserted = False
        for idx, num in enumerate(maxCandidates):
            if number > num:
                maxCandidates.insert(idx,number)
                numberInList += 1
                inserted = True
                if len(maxCandidates) > n:
                    maxCandidates.pop()
                break
        if inserted == False and numberInList < n:
            maxCandidates.append(number)
            numberInList += 1
    return maxCandidates


