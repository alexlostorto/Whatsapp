# Use Regex
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
            for username, number in dailyMessages.items():
                print(f"{username}: {number:,}")
            for username, number in dailyTextCounter.items():
                print(f"Times {username} said '{textToFind}': {number:,}")
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
