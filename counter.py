import os
import re


def countFiles(path):
    totalMessages = 0

    messages = {}

    regex = "\d{2}\/\d{2}\/\d{4},{1} {1}\d{2}:{1}\d{2} {1}-{1} {1}"

    with open(path, encoding="utf8") as textfile:
        for line in textfile:
            position = re.search(regex, line)
            if position is not None and line.count(':') >= 2:
                totalMessages += 1
                username = ":".join(line.split(':', 2)[:2])[position.end():]
                if username in messages:
                    messages[username] += 1
                else:
                    messages[username] = 1

    for username, number in messages.items():
        print(f"{username}: {number}")

    print(f"Total messages: {totalMessages}")


def openRoot(root):
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(".txt"):
                print("---STATISTICS---")
                countFiles(os.path.join(path, file))
                print("\n\n")


openRoot(os.path.dirname(os.path.abspath(__file__)))
