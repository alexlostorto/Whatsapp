import os
import re


def countMessages(path, logDate=False, textCounter=False):
    totalMessages = 0
    totalTextCount = 0

    messages = {}
    textCount = {}

    regex = "\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - "

    if textCounter:
        textToFind = input("Text to count: ")

    print("\n\n---STATISTICS---")

    with open(path, encoding="utf8") as textfile:
        date = ''
        dailyMessages = {}
        dailyTextCounter = {}
        for line in textfile:
            position = re.search(regex, line)
            if position is not None and line.count(':') >= 2:
                totalMessages += 1
                username = ":".join(line.split(':', 2)[:2])[position.end():]
                message = ":".join(line.split(':', 2)[2:])[1:]
                if username in messages:
                    messages[username] += 1
                else:
                    messages[username] = 1

                # Daily message counter
                if logDate:
                    if username in dailyMessages:
                        dailyMessages[username] += 1
                    else:
                        dailyMessages[username] = 1

                # Text counter
                if textCounter and textToFind.lower() in message.lower():
                    totalTextCount += 1
                    if username in textCount:
                        textCount[username] += 1
                    else:
                        textCount[username] = 1
                    if username in dailyTextCounter:
                        dailyTextCounter[username] += 1
                    else:
                        dailyTextCounter[username] = 1

                if ":".join(line.split(':', 2)[:2])[:10] != date:
                    if date == '':
                        date = ":".join(line.split(':', 2)[:2])[:10]
                        continue
                    print(date)
                    date = ":".join(line.split(':', 2)[:2])[:10]
                    for username, number in dailyMessages.items():
                        print(f"{username}: {number:,}")
                    for username, number in dailyTextCounter.items():
                        print(f"Times {username} said '{textToFind}': {number:,}")
                    dailyMessages = {}
                    dailyTextCounter = {}
                    print()

        if logDate:
            print(date)
            date = ":".join(line.split(':', 2)[:2])[:10]
            for username, number in dailyMessages.items():
                print(f"{username}: {number:,}")
            dailyMessages = {}
            print()

    if logDate:
        print("\n---TOTAL---")
    for username, number in messages.items():
        print(f"{username}: {number:,}")
    for username, number in textCount.items():
        print(f"Times {username} said '{textToFind}': {number:,}")

    print(f"Total messages: {totalMessages:,}")
    if textCounter:
        print(f"Total times '{textToFind}' was said: {totalTextCount:,}")


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

    def yesNo(question):
        userInput = input(question)
        print()

        while True:
            # Check input is acceptable
            if userInput == '':
                print(f"Don't leave me empty!")
                userInput = input(question)
            elif userInput.lower() in ['y', 'ye', 'yes', 'yeah']:
                return True
            elif userInput.lower() in ['n', 'no', 'nop', 'nope']:
                return False

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

    options = [
        "displayDays",
        "textCounter"
    ]

    parameters = []

    # Choose function
    for i in range(len(options)):
        parameters.append(yesNo(f"Do you want to use {options[i]}: "))

    countMessages(os.path.join(txtFiles[file-1][0], txtFiles[file-1][1]), *parameters)
    print("\n")

    input("Press ENTER to exit")


openRoot(os.path.dirname(os.path.abspath(__file__)))
