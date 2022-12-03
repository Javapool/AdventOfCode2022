from ctypes import util
import utilities
import functools

def main():
    data = utilities.readFile("input.txt")
    list = data.splitlines()
    agg = aggregate(list)
    print(agg) 
    max3 = utilities.findMaxNResults(agg,3)
    print(max3)
    print(functools.reduce(lambda a,b:a+b,max3))

def aggregate(list):
    aggregatedList = []
    curr = 0
    for number in list:
        if number == '':
            aggregatedList.append(curr)
            curr = 0
        else:
            curr += int(number)
    return aggregatedList




if __name__== "__main__" :
    main()