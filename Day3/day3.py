import fileinput


inputFile = open('input.txt').read().strip()



# check 3x3 area for symbol per number
# if number is near symbol, add left and right to list [.,1,2,3,.]
# add to sum

lines = []

# add each line to the list of lines
for line in inputFile.split('\n'):
    lines.append(line)


for i in range(len(lines)):
    # print(lines[i])
    # check first line for each character
    chars = []
    for char in lines[i]:
        chars.append(char)

    # check if line above/current/below has a character next to it or diagonally
    for j in range(len(chars)):
        if chars[j].isdigit():
            # check left of digit (make sure it is not out of index)
            if j-1 >= 0 and chars[j-1].isdigit():
                print(chars[j-1])

            # check right of digit (make sure it is not out of index)
            if j+1 <= len(chars)-1 and chars[j+1].isdigit():
                print(chars[j+1])



            #check above line (make sure it exists)
            if i-1 >= 0:
                print()
                # get the chars of that line

            #check below line (make sure it exists)
            if i+1 >= len(lines)-1:
                print()


# add numbers left and right to the number
# add the number to the sum

