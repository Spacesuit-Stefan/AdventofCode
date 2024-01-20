import fileinput

inputFile = open('input.txt')
lines = inputFile.readlines()


# can check on index because colors order changes
cubes = [12, 13, 14]  # 12 Red 13 Green 14 Blue
games = []
testlist = [[1,2],[3,4]]




def fillGames():
    i= 1
    for line in lines:
        newline = line.split(':')
        for line in newline[1::2]:
            splittedline = line.split(';')
            games.append([("Game"+ str(i)), line])
            i += 1

def possible():
    for game in games:
        print(game[0])
        matches = game[1].split(';')
        for match in matches:
            cubes = match.split(',')
            print(cubes)

        # print(game[1])




fillGames()
possible()
# print(games)



fileinput.close()