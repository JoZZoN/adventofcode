lineValues=[]
temp=[]

with open(r"C:\Users\jmccallb\OneDrive - Syracuse University\Documents\Personal\Projects\adventofcode\Inputs\12-1-23part1.txt") as f:
    for line in f:
        for character in line:
            if character.isdigit():
                temp.append(character)

        lineValues.append(int(str(temp[0]) + str(temp[-1])))
        temp=[]

outputNum=0
for number in lineValues:
    outputNum+=number

print(outputNum)