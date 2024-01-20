import fileinput
import re

inputFile = open('input.txt')
lines = inputFile.readlines()


# can check on index because colors order changes
cubes = [12, 13, 14]  # 12 Red 13 Green 14 Blue
cubescolors = ["red","green","blue"]
games = []


def matchNumber(number,index):
    if number <= cubes[index]:
        return True
    else:
        return False
def getColor(color):
    green = color[-5:]
    if green in cubescolors:
        return cubescolors.index(green)
    blue = color[-4:]
    if blue in cubescolors:
        return cubescolors.index(blue)
    red = color[-3:]
    if red in cubescolors:
        return cubescolors.index(red)

def fillGames():
    i= 1
    for line in lines:
        if(line[-1:] == '\n'):
            line = line[:-1]
        newline = line.split(':')
        for line in newline[1::2]:
            splittedline = line.split(';')
            games.append([("Game"+ str(i)), line])
            i += 1

def checkMatches(match):
        res = re.split('(\d+)', match)
        index = getColor(res[2])
        return matchNumber(int(res[1]), index)

def allTrue(results):
    for result in results:
        if result == False:
            return False
    return True
def possible():
    finalresult = 0
    for game in games:
        possible = True
        print(game[0])
        currentgame = re.split('(\d+)', game[0])
        matches = game[1].split(';')
        for match in matches:
            values = match.split(',')
            for value in values:
                # In game 1, three sets of cubes are revealed from the bag (and then put back again)
                # add all the red-green-blue up and check if its not greater then
                result = checkMatches(value)
                if result == False:
                    possible = False
                    break


        if possible:
            finalresult += int(currentgame[1])
            print(currentgame[1])
            print(finalresult)

    return finalresult
        # print(game[1])




fillGames()

print(possible())



fileinput.close()