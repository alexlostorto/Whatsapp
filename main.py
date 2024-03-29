# Relative paths
import os

from src.inputs import chooseFile, chooseOptions
from src.chats import getChats
from src.counter import countMessages


countOptions = {
    'daily-messages': False,
    'text-count': False
}


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    txtFiles = getChats(directory)
    file = chooseFile(txtFiles)
    chooseOptions(countOptions)
    filePath = os.path.join(txtFiles[file-1][0], txtFiles[file-1][1])

    countMessages(filePath, countOptions)
    input("\nPress ENTER to exit")


if __name__ == '__main__':
    main()
