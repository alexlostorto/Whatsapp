# Use Regex
import re


REGEX = "\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - "  # Eg: '18/02/2023, 18:47 - '

totalMessages = 0
date = ''


def countMessages(path, logDate=False, textCounter=False):
    totalTextCount = 0

    messages = {}
    textCount = {}
    dailyMessages = {}
    dailyTextCounter = {}

    if textCounter:
        textToFind = input("Text to count: ")

    print("\n\n---STATISTICS---")

    with open(path, encoding="utf8") as textfile:
        for line in textfile:
            username, message = getMessage(line)

            if username is None or message is None:
                continue

            updateMessageCounter(username, messages)

            # Text counter
            if textCounter and textToFind.lower() in message.lower():
                totalTextCount += 1
                updateMessageCounter(username, textCount)

                if logDate:
                    updateMessageCounter(username, dailyTextCounter)

            # Daily message counter
            if logDate:
                dailyMessages, dailyTextCounter = updateDailyMessages(line, username, textToFind, dailyMessages, dailyTextCounter)

        if logDate:
            printStatistics(username, textToFind, dailyMessages, dailyTextCounter)

    if logDate:
        print("\n---TOTAL---")
    for username, number in messages.items():
        print(f"{username}: {number:,}")
    for username, number in textCount.items():
        print(f"Times {username} said '{textToFind}': {number:,}")

    print(f"Total messages: {totalMessages:,}")

    if textCounter:
        print(f"Total times '{textToFind}' was said: {totalTextCount:,}")


def getMessage(line):
    global totalMessages

    position = re.search(REGEX, line)

    if position is not None and line.count(':') >= 2:
        totalMessages += 1
        username = ":".join(line.split(':', 2)[:2])[position.end():]
        message = ":".join(line.split(':', 2)[2:])[1:]

        return [username, message]
    else:
        return [None, None]


def updateDailyMessages(line, username, textToFind, dailyMessages, dailyTextCounter):
    global date

    updateMessageCounter(username, dailyMessages)

    if ":".join(line.split(':', 2)[:2])[:10] != date:
        if date == '':
            date = ":".join(line.split(':', 2)[:2])[:10]
            return dailyMessages, dailyTextCounter

        printStatistics(username, textToFind, dailyMessages, dailyTextCounter)

        date = ":".join(line.split(':', 2)[:2])[:10]
        dailyMessages = {}
        dailyTextCounter = {}

    return dailyMessages, dailyTextCounter


def updateMessageCounter(username, counterDict):
    if username in counterDict:
        counterDict[username] += 1
    else:
        counterDict[username] = 1


def printStatistics(username, textToFind, dailyMessages, dailyTextCounter):
    print(date)

    for username, number in dailyMessages.items():
        print(f"{username}: {number:,}")

    for username, number in dailyTextCounter.items():
        print(f"Times {username} said '{textToFind}': {number:,}")

    print()
