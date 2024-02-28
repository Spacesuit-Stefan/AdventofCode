import fileinput


inputFile = open('input.txt').read().strip()



# check 3x3 area for symbol per number
# if number is near symbol, add left and right to list [.,1,2,3,.]
# add to sum

lines = []
partSum: int = 0


    # add each line to the list of lines
for line in inputFile.split('\n'):
    lines.append(line)

def checkSymbol(charachter):
    if (charachter == '.'):
        return False
    if (charachter.isdigit()):
        return False
    return True

def checkDigit(charachter):
    if(charachter.isdigit()):
        return True
    return False

def checkIndex(row, index):
    if(row < 0 < len(lines)):
        return False
    if (0 <= index < len(lines[row])):
        return True
    return False

def addTemp(row,index):
    if (checkIndex(row, index)):
        if (checkDigit(lines[row][index])):
            return lines[row][index]
    return None

def checkLeft(row,index):
    checkLeft = True
    leftIndex = index
    tempNumber = []
    leftnumber = addTemp(row, leftIndex)
    if (leftnumber != None):
        tempNumber.insert(0, leftnumber)

    while (checkLeft):
        leftIndex = leftIndex - 1
        leftnumber = addTemp(row, leftIndex)
        if (leftnumber != None):
            tempNumber.insert(0, leftnumber)
        else:
            return tempNumber

def checkRight(row,index):
    checkRight = True
    rightIndex = index
    tempNumber = []
    while (checkRight):
        rightIndex = rightIndex + 1
        rightnumber = addTemp(row, rightIndex)
        if ( rightnumber!= None):
            tempNumber.append(rightnumber)
        else:
            return tempNumber


def checkAbove(row,index):
    global partSum
    newRow = row-1
    leftIndex = index
    rightIndex = index -1
    tempNumber = []
    leftnumbers = checkLeft(newRow, index)
    if (leftnumbers != None):
        tempNumber.extend(leftnumbers)
    #print(tempNumber, "aboveline2")
    middlenumber = addTemp(newRow, index)
    if (middlenumber == None):
        if (len(tempNumber) > 0):
            joinedList = int("".join(tempNumber))
            #print(joinedList)
            partSum += joinedList
            tempNumber = []

    rightnumbers = checkRight(newRow, index)
    if (rightnumbers != None):
        tempNumber.extend(rightnumbers)
    #print(tempNumber, "aboveline2")
    if (len(tempNumber) > 0):
        joinedList = int("".join(tempNumber))
        #print(joinedList)
        partSum += joinedList


def checkSameLine(row,index):
    global partSum
    leftIndex = index
    rightIndex = index
    tempNumber = []
    leftnumbers = checkLeft(row, index)
    if (leftnumbers != None):
        tempNumber.extend(leftnumbers)
    #print(tempNumber, "sameline1")
    if (len(tempNumber) > 0):
        joinedList = int("".join(tempNumber))
        partSum += joinedList


    tempNumber = []
    rightnumbers = checkRight(row, index)
    if (rightnumbers != None):
        tempNumber.extend(rightnumbers)
    #print(tempNumber, "sameline2")
    if (len(tempNumber) > 0):
        joinedList = int("".join(tempNumber))
        partSum += joinedList



def checkBelow(row,index):
    global partSum
    # go one below current row
    newRow = row + 1
    #[1,0,0]
    tempNumber = []
    leftnumbers = checkLeft(newRow, index)
    if(leftnumbers != None):
        tempNumber.extend(leftnumbers)

    middlenumber = addTemp(newRow, index)
    if (middlenumber == None):
        if (len(tempNumber) > 0):
            joinedList = int("".join(tempNumber))
            partSum += joinedList
            tempNumber = []

    rightnumbers = checkRight(newRow, index)
    if (rightnumbers != None):
        tempNumber.extend(rightnumbers)


    #print(tempNumber, "below1")
    if (len(tempNumber) > 0):
        joinedList = int("".join(tempNumber))
        #print (joinedList)
        partSum += joinedList
        #print(partSum)


for row in range(0, len(lines)-1):
    for index in range(0, len(lines[row])-1):
        if(checkSymbol(lines[row][index])):
            checkAbove(row, index)
            checkSameLine(row, index)
            checkBelow(row, index)


print(partSum)