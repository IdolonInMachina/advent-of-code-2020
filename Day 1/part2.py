
# Get the personalised input
inputArray = []
currentInput = input()
while currentInput != 'finished':
    inputArray.append(int(currentInput))
    currentInput = input()

print(inputArray)

for num in inputArray:
    for innerNum in inputArray:
        for innerMostNum in inputArray:
            if (num + innerNum + innerMostNum == 2020):
                print(f"Result: {num * innerNum * innerMostNum}")
