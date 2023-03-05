import os
import re


def countMessages(path, logDate=False):
    totalMessages = 0

    messages = {}

    regex = "\d{2}\/\d{2}\/\d{4},{1} {1}\d{2}:{1}\d{2} {1}-{1} {1}"

    with open(path, encoding="utf8") as textfile:
        date = ''
        dailyMessages = {}
        for line in textfile:
            position = re.search(regex, line)
            if position is not None and line.count(':') >= 2:
                totalMessages += 1
                username = ":".join(line.split(':', 2)[:2])[position.end():]
                if username in messages:
                    messages[username] += 1
                else:
                    messages[username] = 1

                # Daily message counter
                if not logDate:
                    continue

                if username in dailyMessages:
                    dailyMessages[username] += 1
                else:
                    dailyMessages[username] = 1
                if ":".join(line.split(':', 2)[:2])[:10] != date:
                    date = ":".join(line.split(':', 2)[:2])[:10]
                    print(date)
                    for username, number in dailyMessages.items():
                        print(f"{username}: {number:,}")
                    dailyMessages = {}
                    print()

    if logDate:
        print("\n---TOTAL---")
    for username, number in messages.items():
        print(f"{username}: {number:,}")

    print(f"Total messages: {totalMessages:,}")


def openRoot(root):
    def getInput(array, question):
        userInput = input(question)
        print()

        while True:
            # check input is acceptable
            if not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(array):
                print(f"Input has to be a number 1-{len(array)}")
                userInput = input(question)
                continue
            else:
                # chooses file
                userInput = int(userInput)
                return userInput

    txtFiles = []
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(".txt"):
                txtFiles.append([path, file])

    # Choose text files
    for i in range(len(txtFiles)):
        print(f"{i+1}) {txtFiles[i][1]}")
    file = getInput(txtFiles, "Choose which file you want to use: ")
    print(f"You chose '{txtFiles[file-1][1]}'\n")

    functions = [
        "countMessages",
        "displayDays"
    ]

    # Choose function
    for i in range(2):
        print(f"{i+1}) {functions[i]}")
    function = getInput(functions, "Choose which function you want to use: ")
    print(f"You chose '{functions[function-1]}'\n")

    print("\n\n---STATISTICS---")
    if function == 1:
        countMessages(os.path.join(txtFiles[file-1][0], txtFiles[file-1][1]))
    elif function == 2:
        countMessages(os.path.join(txtFiles[file-1][0], txtFiles[file-1][1]), True)
    print("\n\n")


openRoot(os.path.dirname(os.path.abspath(__file__)))
