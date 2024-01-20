import fileinput

inputFile = open('input.txt')
lines = inputFile.readlines()
sum = 0



numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberWordsReversed= []


def findLetter(letter, lst):
    return any(letter in word for word in lst)
def firstNumber(lineinput):
    letterList = [x for x in lineinput]
    newList = ""
    for letter in letterList:
        if letter.isdigit():
            return letter
        else:
            newList += letter
            if findLetter(newList, numberWords):
                if newList in numberWords:
                    return numberWords.index(newList)+1
            else:
                newList = newList[1:]

def lastNumber(lineinput):
    letterList = [x for x in lineinput]
    letterList.reverse()
    newList = ""
    for letter in letterList:
        if letter.isdigit():
            return letter
        else:
            newList += letter
            if findLetter(newList, numberWordsReversed):
                if newList in numberWordsReversed:
                    return numberWordsReversed.index(newList) + 1
            else:
                newList = newList[1:]

for word in numberWords:
    letters = [x for x in word]
    letters.reverse()
    newWord= ""
    for letter in letters:
        newWord += letter
    numberWordsReversed.append(newWord)

for line in lines:
    firstnumber = firstNumber(line)
    lastnumber = lastNumber(line)


    combinednumber = str(firstnumber) + str(lastnumber)
    #  print (combinednumber)
    sum += int(combinednumber)
    print(sum)


    #print(line)

fileinput.close()


