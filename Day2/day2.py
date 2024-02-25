import fileinput
import re

inputFile = open('input.txt')
lines = inputFile.readlines()


# can check on index because colors order changes
cubes = [12, 13, 14]  # 12 Red 13 Green 14 Blue
cubescolors = ["red","green","blue"]
games = []


D = open('input.txt').read().strip()
#only 12 red cubes, 13 green cubes, 14 blue cubes
def correctAnswer():
    ans = 0
    for line in D.split('\n'):
        ok = True
        id_, line = line.split(':')
        for event in line.split(';'):
            for balls in event.split(','):
                n,color = balls.split()
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color):
                    ok = False
        if ok:
            ans += int(id_.split()[-1])
            print(id_)
    print(ans)


# def matchNumber(number,index):
#     if number <= cubes[index]:
#         return True
#     else:
#         return False
# def getColor(color):
#     green = color[-5:]
#     if green in cubescolors:
#         return cubescolors.index(green)
#     blue = color[-4:]
#     if blue in cubescolors:
#         return cubescolors.index(blue)
#     red = color[-3:]
#     if red in cubescolors:
#         return cubescolors.index(red)
#
# def fillGames():
#     i= 1
#     for line in lines:
#         if(line[-1:] == '\n'):
#             line = line[:-1]
#         newline = line.split(':')
#         for line in newline[1::2]:
#             splittedline = line.split(';')
#             games.append([("Game"+ str(i)), line])
#             i += 1
#
# # def checkMatches(match):
# #         res = re.split('(\d+)', match)
# #         index = getColor(res[2])
# #         return matchNumber(int(res[1]), index)
#
# def allTrue(results):
#     for result in results:
#         if result == False:
#             return False
#     return True
# def possible():
#     finalresult = 0
#     for game in games:
#         #red,green,blue
#         colors =[0,0,0]
#
#         possible = True
#         print(game[0])
#         currentgame = re.split('(\d+)', game[0])
#         matches = game[1].split(';')
#         for match in matches:
#             if possible != True:
#                 break
#             values = match.split(',')
#             for value in values:
#                 # In game 1, three sets of cubes are revealed from the bag (and then put back again)
#                 # add all the red-green-blue up and check if its not greater then
#
#                 # split number and word
#                 res = re.split('(\d+)', value)
#                 index = getColor(res[2])
#                 #print(res)
#
#                 # add up the number to color
#                 colors[index] += int(res[1])
#                 #print(colors)
#
#                 # matchnumber
#                 result = matchNumber(colors[index], index)
#                 #print(result)
#                 if result == False:
#                     possible = False
#                     break
#
#
#         if possible:
#             finalresult += int(currentgame[1])
#             print(currentgame[1])
#             print(finalresult)
#
#     return finalresult
#         # print(game[1])





correctAnswer()


fileinput.close()