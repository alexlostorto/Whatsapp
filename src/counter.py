import re

REGEX = "\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - "  # Eg: '18/02/2023, 18:47 - '

date = ''
totalMessages = 0
totalTextCount = 0
totalWordCount = 0
messages = {}
textCount = {}
dailyMessages = {}
dailyTextCounter = {}
wordCount = {}  # Tracks word count per user
dailyWordCount = {}  # Tracks daily word count per user
def countMessages(path, countOptions):
    if countOptions['text-count']:
        textToFind = input("Text to count: ")

    print("\n\n---STATISTICS---")

    with open(path, encoding="utf8") as textfile:
        for line in textfile:
            username, message = getMessage(line)

            if username is None or message is None:
                continue

            # Message counter
            updateMessageCounter(username, messages)
            
            # Word counter
            updateWordCounter(username, message, wordCount)

            # Text counter
            if countOptions['text-count']:
                countText(countOptions, username, message, textToFind)

            # Daily message counter
            if countOptions['daily-messages']:
                updateDailyMessages(line, username, textToFind)

    if countOptions['daily-messages']:
        printStatistics(username, textToFind, dailyMessages, dailyTextCounter, dailyWordCount)
        print("\n---TOTAL---")
    
    for username, number in messages.items():
        print(f"{username}: {number:,}")
    for username, number in textCount.items():
        print(f"Times {username} said '{textToFind}': {number:,}")
    # for username, number in wordCount.items():
    #     print(f"Total words by {username}: {number:,}")

    print(f"Total messages: {totalMessages:,}")
    print(f"Total words: {totalWordCount:,}")

    if countOptions['text-count']:
        print(f"Total times '{textToFind}' was said: {totalTextCount:,}")

def countText(countOptions, username, message, textToFind):
    global totalTextCount

    if textToFind.lower() in message.lower():
        totalTextCount += 1
        updateMessageCounter(username, textCount)

        if countOptions['daily-messages']:
            updateMessageCounter(username, dailyTextCounter)

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

def updateDailyMessages(line, username, textToFind):
    global date, dailyMessages, dailyTextCounter, dailyWordCount

    updateMessageCounter(username, dailyMessages)
    updateWordCounter(username, getMessage(line)[1], dailyWordCount)

    if ":".join(line.split(':', 2)[:2])[:10] != date:
        if date == '':
            date = ":".join(line.split(':', 2)[:2])[:10]
            return dailyMessages, dailyTextCounter, dailyWordCount

        printStatistics(username, textToFind, dailyMessages, dailyTextCounter, dailyWordCount)

        date = ":".join(line.split(':', 2)[:2])[:10]
        dailyMessages = {}
        dailyTextCounter = {}
        dailyWordCount = {}

    return dailyMessages, dailyTextCounter, dailyWordCount

def updateMessageCounter(username, counterDict):
    if username in counterDict:
        counterDict[username] += 1
    else:
        counterDict[username] = 1

def updateWordCounter(username, message, counterDict):
    global totalWordCount
    word_count = len(message.split())
    totalWordCount += word_count

    if username in counterDict:
        counterDict[username] += word_count
    else:
        counterDict[username] = word_count

def printStatistics(username, textToFind, dailyMessages, dailyTextCounter, dailyWordCount):
    print(date)

    for username, number in dailyMessages.items():
        print(f"{username}: {number:,}")
    for username, number in dailyTextCounter.items():
        print(f"Times {username} said '{textToFind}': {number:,}")
    for username, number in dailyWordCount.items():
        print(f"Total words by {username}: {number:,}")

    print()
