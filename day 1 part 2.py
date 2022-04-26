# find inputs
file = open('/home/mark/PycharmProjects/adventOfCode/sonarSweepInput.txt', 'r')
dataArray = []
total = 0

# test by reading file
dataString = file.read()
dataArray = dataString.split('\n')

# convert to integer
def toInt(inputString):
    return int(inputString)

for i in range(len(dataArray) - 1):
    if i > 2:
        num1 = toInt(dataArray[i - 3])
        num2 = toInt(dataArray[i - 2])
        num3 = toInt(dataArray[i - 1])
        num4 = toInt(dataArray[i])

        window1 = num1 + num2 + num3
        window2 = num2 + num3 + num4

        if window1 < window2:
            total += 1

print(total)

# close file
file.close()
